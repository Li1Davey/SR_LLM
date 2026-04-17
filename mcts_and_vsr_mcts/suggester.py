import os
import re
import json
import datetime
from openai import OpenAI


def _get_client():
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def filter_best_for_prompt(best_expressions: list, max_show: int = 15, max_expr_len: int = 120) -> list:
    """
    Filter best expressions shown to the LLM by character length.
    Preserves compact high-power expressions like X0**9/(X1+C) while
    stripping massive sympy-expanded forms that are noise for the LLM.
    Falls back to the shortest available if nothing passes the filter.
    """
    clean = [e for e in best_expressions if len(e) <= max_expr_len]
    result = clean if clean else sorted(best_expressions, key=len)
    return result[:max_show]


def build_prompt(equation_name, current_rules, best_expressions, nvars, operators_set, vars_range=None, max_suggestions=5, base_rules=None):
    """
    Build a plain-text prompt for the LLM to extract repeating subexpressions
    from the best expressions and encode them as new terminal production rules.

    The LLM's job is pattern extraction, not grammar design — it should look
    at what subexpressions appear repeatedly across the best expressions and
    suggest those as new A-> terminal rules so the MCTS can reuse them directly.
    """
    # Variable range summary
    range_lines = []
    transcendental_ok = True

    if vars_range:
        for i, vr in enumerate(vars_range):
            if not isinstance(vr, dict) or 'range' not in vr:
                continue
            lo, hi = vr['range']
            only_pos = vr.get('only_positive', False)
            notes = []
            if only_pos:
                notes.append("always positive")
            if hi > 1e6:
                notes.append("very large scale — likely appears in denominator")
            elif hi <= 10:
                notes.append("small scale — may appear raised to higher powers")
            if only_pos and lo >= 0:
                transcendental_ok = False
            note_str = f" ({', '.join(notes)})" if notes else ""
            range_lines.append(f"  X{i}: [{lo}, {hi}]{note_str}")

    range_block = "Variable ranges:\n" + "\n".join(range_lines) if range_lines else "Variable ranges: (not available)"

    base_rules_text = ",  ".join(base_rules) if base_rules else ",  ".join(current_rules)

    rules_text = "\n".join(current_rules) if current_rules else "(none)"
    ops_text   = ", ".join(sorted(list(operators_set))) if operators_set else "(none)"
    expr_text  = "\n".join(best_expressions) if best_expressions else "(none)"

    trig_warning = ""
    if not transcendental_ok:
        trig_warning = (
            "IMPORTANT: All variables are strictly positive. "
            "Do not suggest sin, cos, exp, or log rules.\n\n"
        )

    prompt = (
        f"You are assisting a symbolic regression system in discovering a physical equation.\n"
        f"The system builds expressions by repeatedly replacing A using production rules.\n"
        f"For example, given base rules such as:\n"
        f"  {base_rules_text}\n"
        f"Each A is independently replaced until no A remains, forming a full expression.\n\n"
        f"=== CONTEXT ===\n"
        f"Equation      : {equation_name}\n"
        f"Variables     : X0..X{nvars - 1}\n"
        f"{range_block}\n"
        f"Operators     : {ops_text}\n\n"
        f"=== BEST EXPRESSIONS (highest reward first) ===\n"
        f"{expr_text}\n\n"
        f"=== CURRENT PRODUCTION RULES (DO NOT REPEAT THESE) ===\n"
        f"{rules_text}\n\n"
        f"{trig_warning}"
        f"=== STRUCTURAL ANALYSIS INSTRUCTIONS ===\n"
        f"Step 1 — Strip constants: mentally replace every numeric coefficient with C.\n"
        f"Step 2 — Find skeletons: what is the shape of each expression ignoring C?\n"
        f"  Parentheses are grouping only — '(A)/(A)', 'A/A', and '(A/A)' are the same skeleton.\n"
        f"  e.g. 'C*A + C*A'  ->  skeleton is '(A+A)'\n"
        f"  e.g. 'C*A/A'      ->  skeleton is 'A/A'\n"
        f"  e.g. 'C*A/(A+A)'  ->  skeleton is 'A/(A+A)'\n"
        f"Step 3 — Find recurring sub-skeletons across 3+ expressions. Look for ALL pattern types:\n"
        f"  Ratio    : if 'A/A' recurs -> 'A->A/A',       if 'A/(A+A)' recurs -> 'A->A/(A+A)'\n"
        f"  Power    : if 'A**A' recurs -> 'A->A**A',      if 'A**A*A' recurs -> 'A->A**A*A'\n"
        f"  Product  : if 'A*A' recurs -> 'A->A*A',        if 'A*A*A' recurs -> 'A->A*A*A'\n"
        f"  Mixed    : if 'A*A/A' recurs -> 'A->A*A/A',    if '(A+A)/A' recurs -> 'A->(A+A)/A'\n"
        f"  Before suggesting a rule, strip all redundant parentheses from it, then check if\n"
        f"  the result already appears — with or without parentheses — in the existing rules.\n"
        f"  Only suggest it if the stripped form is genuinely absent from the existing rules.\n"
        f"Step 4 — Encode only the recurring sub-skeletons as new rules.\n\n"
        f"=== YOUR TASK ===\n"
        f"Following Steps 1-4 above, identify subexpressions that recur across the best\n"
        f"expressions and encode each as a new rule in the format 'A-><subexpression>',\n"
        f"where the right-hand side contains only A and operators — variables and constants\n"
        f"are reached through existing rules.\n\n"
        f"=== OUTPUT FORMAT ===\n"
        f"- Up to {max_suggestions} new rules, one per line, starting with 'A->'\n"
        f"- DO NOT repeat any of the current rule already listed above\n"
        f"- Output only the rules, one per line, no explanation\n"
    )

    return prompt

def call_openai(prompt, model="gpt-4.1-mini", temperature=0.2):
    """Send the prompt to OpenAI and return the model's plain text response."""
    client = _get_client()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that outputs CFG production rules when asked."},
            {"role": "user",   "content": prompt}
        ],
        temperature=temperature,
    )
    try:
        text = response.choices[0].message.content
    except Exception:
        text = str(response)
    return text.strip()


def parse_and_validate_rules(response_text, existing_rules, operators_set, nvars, non_terminal='A'):
    """
    Parses the raw LLM response and splits rules into valid and rejected lists.
    Acts as the syntax gate — enforcing correct format, no duplicates, and only
    allowed tokens before any rule is passed downstream.

    Checks:
    - Lines must start with '<non_terminal>->'
    - Reject duplicates (whitespace-normalized) against existing_rules
    - RHS must contain only allowed tokens
    - Intra-response duplicates also caught
    """
    existing = set(existing_rules or [])
    ops      = set(operators_set or [])

    allowed_vars   = {f"X{i}" for i in range(max(0, nvars))}
    allowed_tokens = {"C", non_terminal} | allowed_vars | ops

    ALLOWED_PUNCT = frozenset({"+", "-", "*", "/", "(", ")", ",", "**"})

    # Whitespace-normalize existing rules for dedup
    normalized_existing = {r.replace(' ', '') for r in existing}

    valid    = []
    rejected = []

    for raw_line in (response_text or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        prefix = f"{non_terminal}->"
        if not line.startswith(prefix):
            rejected.append(line)
            continue

        rhs = line[len(prefix):].strip()
        if not rhs:
            rejected.append(line)
            continue

        line = line.replace(' ', '')
        rhs  = rhs.replace(' ', '')

        if line in normalized_existing:
            rejected.append(line)
            continue

        tokens = re.findall(
            r"\*\*"
            r"|[A-Za-z_][A-Za-z0-9_]*"
            r"|[0-9]+(?:\.[0-9]+)?"
            r"|[+\-*/(),]",
            rhs
        )

        malformed = False
        for tok in tokens:
            if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", tok):
                continue
            if tok in ALLOWED_PUNCT:
                continue
            if tok in allowed_tokens:
                continue
            malformed = True
            break

        if malformed:
            rejected.append(line)
            continue

        valid.append(line)
        # Catch duplicates within the same LLM response
        normalized_existing.add(line)

    return valid, rejected


def is_domain_safe(rule: str, vars_range: list) -> bool:
    """
    Acts as the semantic gate after syntax validation — rejects rules that are
    mathematically unsafe given the variable domains, such as log/sqrt when
    values can be zero, or trig functions over very large ranges.
    """
    if not vars_range:
        return True

    valid_ranges = [r for r in vars_range if isinstance(r, dict) and 'range' in r]
    if not valid_ranges:
        return True

    has_negatives = any(r['range'][0] < 0  for r in valid_ranges)
    has_zero = any(r['range'][0] <= 0 for r in valid_ranges)

    if has_negatives or has_zero:
        for pattern in ('log', 'sqrt', 'A**0.', 'A**C'):
            if pattern in rule:
                print(f">>> [is_domain_safe] Rejected rule {rule!r} "
                      f"— {pattern!r} unsafe when domain includes zero/negatives")
                return False

    # Trig safety — sin/cos over ranges >> 2*pi produce numerical noise
    TRIG_FNS = ('sin', 'cos')
    for i, vr in enumerate(valid_ranges):
        vmin, vmax = vr['range']
        if vmax > 100:
            var = f"X{i}"
            for fn in TRIG_FNS:
                if f"{fn}({var})" in rule:
                    print(f">>> [is_domain_safe] Rejected rule {rule!r} "
                          f"— {fn}({var}) is noise at range [{vmin}, {vmax}]")
                    return False

    return True


def suggest_rules(equation_name,
                  current_rules,
                  best_expressions,
                  nvars,
                  operators_set,
                  model="gpt-4.1-mini",
                  vars_range=None,
                  temperature=0.2,
                  max_suggestions=5,
                  base_rules=None,
                  log_path="llm_rule_history.log"):
    """
    High-level wrapper that runs the full LLM suggestion pipeline:
    1. Filter best expressions by length to remove bloated sympy expansions
    2. Build prompt with structural hints
    3. Query the LLM
    4. Parse and validate returned rules
    5. Filter domain-unsafe rules
    6. Log the full cycle

    Parameters:
    - equation_name (str)
    - current_rules (list[str])
    - best_expressions (list[str]): pre-sorted by reward descending before this call
    - nvars (int)
    - operators_set (set[str])
    - model (str)
    - vars_range (list[dict] | None)
    - temperature (float)
    - max_suggestions (int)
    - log_path (str | None)

    Returns:
    - valid_rules (list[str])
    - rejected_rules (list[str])
    """

    # Defensive re-parse of vars_range entries that arrive as JSON strings
    if vars_range is not None:
        parsed = []
        for entry in vars_range:
            if isinstance(entry, str):
                try:
                    parsed.append(json.loads(entry))
                except (json.JSONDecodeError, ValueError):
                    parsed.append(entry)
            else:
                parsed.append(entry)
        vars_range = parsed

    # 1. Filter best expressions by length — removes massive sympy-expanded
    #    denominators while preserving compact high-power forms like X0**9/(X1+C)
    filtered_expressions = filter_best_for_prompt(best_expressions)

    # 2. Build the prompt with structural hints
    prompt = build_prompt(
        equation_name,
        current_rules,
        filtered_expressions,
        nvars,
        operators_set,
        vars_range=vars_range,
        max_suggestions=max_suggestions,
        base_rules=base_rules
    )

    # 3. Call the LLM
    raw = call_openai(prompt, model=model, temperature=temperature)

    # 4. Parse and validate
    valid, rejected = parse_and_validate_rules(
        raw,
        existing_rules=current_rules,
        operators_set=operators_set,
        nvars=nvars,
        non_terminal='A'
    )

    # 5. Filter domain-unsafe rules
    if vars_range is not None:
        domain_safe = [r for r in valid if is_domain_safe(r, vars_range)]
        domain_rejected = [r for r in valid if not is_domain_safe(r, vars_range)]

        if domain_rejected:
            print(f">>> [suggest_rules] Rejected {len(domain_rejected)} "
                  f"domain-unsafe rule(s): {domain_rejected}")

        rejected += domain_rejected
        valid = domain_safe

    valid = valid[:max_suggestions]

    # 6. Log the full cycle — includes both the raw and filtered expression lists
    if log_path:
        entry = {
            "timestamp":            datetime.datetime.utcnow().isoformat() + "Z",
            "equation":             equation_name,
            "nvars":                nvars,
            "operators":            sorted(list(operators_set)) if operators_set else [],
            "vars_range":           vars_range,
            "current_rules":        list(current_rules),
            "best_expressions":     list(best_expressions),
            "filtered_expressions": filtered_expressions,
            "prompt":               prompt,
            "raw_response":         raw,
            "valid_rules":          valid,
            "rejected_rules":       rejected,
            "model":                model,
            "temperature":          temperature,
        }
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception:
            pass

    return valid, rejected
