import os
import re
import json
import datetime
from openai import OpenAI


def _get_client():
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def _normalise_rule(rule: str) -> str:
    """
    Strip redundant parentheses from RHS for semantic dedup.
    Ensures A->(A+A) and A->A+A are treated as identical.
    """
    if '->' not in rule:
        return rule.replace(' ', '')
    lhs, rhs = rule.split('->', 1)
    prev = None
    while prev != rhs:
        prev = rhs
        rhs = re.sub(r'$([^()]+)$', r'\1', rhs)
    return f"{lhs}->{rhs}".replace(' ', '')


def _compute_covered_skeletons(current_rules: list) -> set:
    """
    Extract the normalised RHS skeletons already covered by the current grammar.
    Strips constants and variable names to leave pure structural patterns.
    Used to give the model a compact summary of what is already reachable,
    so it can focus on genuine gaps rather than re-deriving known patterns.
    """
    skeletons = set()
    for rule in current_rules:
        if '->' not in rule:
            continue
        rhs = rule.split('->', 1)[1].strip()
        skel = re.sub(r'C\*?', '', rhs)
        skel = re.sub(r'X\d+', '', skel)
        skel = re.sub(r'\s+', '', skel)
        norm = _normalise_rule(f"A->{skel}").replace('A->', '')
        if norm:
            skeletons.add(norm)
    return skeletons


def filter_best_for_prompt(best_expressions: list, max_show: int = 20, max_expr_len: int = 180) -> list:
    """
    Filter best expressions shown to the LLM by character length, then apply a
    skeleton diversity filter so the model sees varied structural patterns rather
    than 20 near-identical linear combinations.

    max_expr_len is 180 so expressions containing sin(X0)**2, X2**2*sin(X0),
    sin(X0)*cos(X0) etc. are not cut — these are exactly the patterns the LLM
    needs to see to suggest power/product/trig-product rules.
    Falls back to the shortest available if nothing passes the length filter.
    """
    clean = [e for e in best_expressions if len(e) <= max_expr_len]
    result = clean if clean else sorted(best_expressions, key=len)

    # Skeleton diversity — keep at most 3 expressions per rough skeleton bucket
    # to avoid showing the model only linear sums of terminals.
    skeleton_counts: dict = {}
    diverse = []
    for expr in result:
        skeleton = re.sub(r'[-+]?[0-9]+\.?[0-9]*[eE]?[-+]?[0-9]*\*?', '', expr)
        skeleton = re.sub(r'X\d+', 'X', skeleton)
        key = skeleton[:40]
        if skeleton_counts.get(key, 0) < 3:
            skeleton_counts[key] = skeleton_counts.get(key, 0) + 1
            diverse.append(expr)
        if len(diverse) >= max_show:
            break

    return diverse if diverse else result[:max_show]


def build_prompt(equation_name, current_rules, best_expressions, nvars, operators_set,
                 vars_range=None, max_suggestions=5, base_rules=None):
    """
    Build a plain-text prompt for the LLM to extract repeating subexpressions
    from the best expressions and encode them as new production rules.

    Key design decisions:
    - The example block uses base_rules only to illustrate grammar mechanics,
      kept short so it does not crowd the current rules list.
    - current_rules are deduplicated and normalised before display.
    - A compact 'already covered skeletons' block gives the model a structural
      summary that is harder to accidentally re-derive than the full rule list.
    - Trig pattern examples are included only when sin/cos are in operators_set.
    - The trig warning only fires for large-range variables, not all positives.
    """
    # --- Variable range block ---
    range_lines = []
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
            note_str = f" ({', '.join(notes)})" if notes else ""
            range_lines.append(f"  X{i}: [{lo}, {hi}]{note_str}")

    range_block = (
        "Variable ranges:\n" + "\n".join(range_lines)
        if range_lines else "Variable ranges: (not available)"
    )

    # --- Base rules example (short, for grammar mechanics only) ---
    base_rules_text = ",  ".join(base_rules) if base_rules else ",  ".join(current_rules[:6])

    # --- Deduplicate current_rules before display ---
    seen_norm = set()
    deduped_rules = []
    for r in current_rules:
        n = _normalise_rule(r)
        if n not in seen_norm:
            seen_norm.add(n)
            deduped_rules.append(r)

    rules_text   = "\n".join(deduped_rules) if deduped_rules else "(none)"
    ops_text     = ", ".join(sorted(list(operators_set))) if operators_set else "(none)"
    expr_text    = "\n".join(best_expressions) if best_expressions else "(none)"

    # --- Covered skeletons summary ---
    covered      = _compute_covered_skeletons(deduped_rules)
    covered_text = ",  ".join(sorted(covered)) if covered else "(none)"

    # --- Trig warning: only for large-range variables ---
    trig_warning = ""
    if vars_range:
        large_range_vars = [
            f"X{i}" for i, vr in enumerate(vars_range)
            if isinstance(vr, dict) and 'range' in vr and vr['range'][1] > 1e6
        ]
        if large_range_vars:
            trig_warning = (
                f"NOTE: Do not suggest sin or cos applied directly to "
                f"{', '.join(large_range_vars)} — those variables span very large ranges "
                f"and trig functions produce numerical noise at that scale.\n\n"
            )

    # --- Trig pattern examples (only when trig is in the operator set) ---
    has_trig = bool({'sin', 'cos'} & set(operators_set or []))

    trig_skeleton_examples = (
        f"  e.g. 'C*sin(X0) + C*cos(X0)'  ->  skeleton is 'sin(A)+cos(A)'\n"
        f"  e.g. 'C*sin(X0)*cos(X0)'       ->  skeleton is 'sin(A)*cos(A)'\n"
        f"  e.g. 'C*sin(X0)**2'            ->  skeleton is 'sin(A)**2'\n"
    ) if has_trig else ""

    trig_pattern_lines = (
        f"  Trig product : if 'sin(A)*cos(A)' recurs  ->  'A->sin(A)*cos(A)'\n"
        f"  Trig power   : if 'sin(A)**2' recurs       ->  'A->sin(A)**2'\n"
        f"  Trig ratio   : if 'A/sin(A)' recurs        ->  'A->A/sin(A)'\n"
    ) if has_trig else ""

    prompt = (
        f"You are assisting a symbolic regression system in discovering a physical equation.\n"
        f"The system builds expressions by repeatedly replacing the non-terminal A using\n"
        f"production rules until no A remains, forming a complete expression.\n"
        f"Example grammar mechanics (base rules only — not the full current grammar):\n"
        f"  {base_rules_text}\n\n"
        f"=== CONTEXT ===\n"
        f"Equation      : {equation_name}\n"
        f"Variables     : X0..X{nvars - 1}\n"
        f"{range_block}\n"
        f"Operators     : {ops_text}\n\n"
        f"=== BEST EXPRESSIONS (highest reward first) ===\n"
        f"{expr_text}\n\n"
        f"=== CURRENT PRODUCTION RULES (ALL ALREADY IN THE GRAMMAR) ===\n"
        f"{rules_text}\n\n"
        f"=== STRUCTURAL PATTERNS ALREADY COVERED ===\n"
        f"{covered_text}\n"
        f"Every pattern listed above is already reachable. Only suggest rules whose\n"
        f"stripped skeleton does NOT appear in the covered list.\n\n"
        f"{trig_warning}"
        f"=== STRUCTURAL ANALYSIS INSTRUCTIONS ===\n"
        f"Step 1 — Strip constants: replace every numeric coefficient with C.\n"
        f"Step 2 — Find skeletons: the shape of each expression ignoring C and variable names.\n"
        f"  Parentheses are grouping only — '(A)/(A)', 'A/A', '(A/A)' are the same skeleton.\n"
        f"  e.g. 'C*A + C*A'    ->  skeleton is 'A+A'\n"
        f"  e.g. 'C*A/A'        ->  skeleton is 'A/A'\n"
        f"  e.g. 'C*A/(A+A)'    ->  skeleton is 'A/A+A'\n"
        f"{trig_skeleton_examples}"
        f"Step 3 — Find recurring sub-skeletons across 3+ expressions:\n"
        f"  Ratio   : 'A/A' recurs        ->  'A->A/A'\n"
        f"  Power   : 'A**2' recurs       ->  'A->A**2'\n"
        f"  Product : 'A*A*A' recurs      ->  'A->A*A*A'\n"
        f"  Mixed   : 'A*A/A' recurs      ->  'A->A*A/A'\n"
        f"{trig_pattern_lines}"
        f"  Check each candidate against the COVERED list above before including it.\n"
        f"Step 4 — Encode only genuinely new recurring sub-skeletons as rules.\n\n"
        f"=== YOUR TASK ===\n"
        f"Identify subexpressions that recur across the best expressions and are NOT already\n"
        f"covered. Encode each as 'A-><subexpression>' where the RHS contains only A,\n"
        f"operators, and function names — variables and constants are reached through\n"
        f"existing terminal rules.\n\n"
        f"=== OUTPUT FORMAT ===\n"
        f"- Up to {max_suggestions} new rules, one per line, starting with 'A->'\n"
        f"- DO NOT suggest any rule whose skeleton already appears in the COVERED list\n"
        f"- A->(A+A) and A->A+A are identical — do not suggest both\n"
        f"- DO NOT suggest rules where a function is applied to itself or nested,\n"
        f"  e.g. exp(exp(A)), sin(cos(A)), log(exp(A)) are all forbidden —\n"
        f"  nesting is achieved naturally by applying single-call rules in sequence\n"
        f"- Output fewer than {max_suggestions} if you cannot find that many genuine new rules\n"
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
    - Reject duplicates (normalised, parenthesis-insensitive) against existing_rules
    - RHS tokens must be one of: non_terminal, C, XN variables, any operator in
      operators_set (including named functions like sin/cos/exp/log/sqrt/tan),
      numeric literals, or punctuation (+, -, *, /, (, ), **)
    - Intra-response duplicates also caught
    - Nested function calls rejected — e.g. exp(exp(A)), sin(cos(A)) (DS)
    """
    existing = set(existing_rules or [])
    ops      = set(operators_set or [])

    allowed_vars = {f"X{i}" for i in range(max(0, nvars))}

    # Any operator that is a valid Python identifier (word token) is allowed as
    # a named function in the RHS — covers sin, cos, exp, log, sqrt, tan, and
    # any custom function the task declares. Symbol operators (+, -, *, /, **)
    # are handled separately via ALLOWED_PUNCT.
    named_ops = {op for op in ops if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', op)}

    allowed_tokens = {"C", non_terminal} | allowed_vars | named_ops

    ALLOWED_PUNCT = frozenset({"+", "-", "*", "/", "(", ")", ",", "**"})

    # Normalised dedup — catches A->A/A when A->(A)/(A) already exists
    normalized_existing = {_normalise_rule(r) for r in existing}

    # Functions that can form dangerous nesting towers when composed in a
    # single rule — e.g. exp(exp(A)), sin(cos(A)), log(exp(A)). The grammar
    # already composes single-call rules naturally through tree expansion so
    # nesting inside one rule adds no new structure and blows up expression
    # depth in a single step.
    NESTABLE_OPS = ['exp', 'sin', 'cos', 'log', 'sqrt', 'tan']

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

        if _normalise_rule(line) in normalized_existing:
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

        # Reject rules containing nested function calls — e.g. exp(exp(A)),
        # sin(cos(A)), log(exp(A)). The grammar composes single-call rules
        # naturally through tree expansion so nesting in a single rule adds
        # no new structure and blows up expression depth in one step.
        nested = False
        for op in NESTABLE_OPS:
            if op not in rhs:
                continue
            # Match this op's call and check if any nestable op appears
            # inside its argument brackets.
            pattern = rf'{op}$[^)]*(?:{"|".join(NESTABLE_OPS)})[^)]*$'
            if re.search(pattern, rhs):
                print(f">>> [parse_and_validate_rules] Rejected rule {line!r} "
                      f"— nested function call detected ({op}(...))")
                nested = True
                break
        if nested:
            rejected.append(line)
            continue

        valid.append(line)
        # Catch intra-response duplicates using the same normalised key
        normalized_existing.add(_normalise_rule(line))

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

    has_negatives = any(r['range'][0] < 0 for r in valid_ranges)
    has_zero      = any(r['range'][0] <= 0 for r in valid_ranges)

    if has_negatives or has_zero:
        for pattern in ('log', 'sqrt', 'A**0.', 'A**C'):
            if pattern in rule:
                print(f">>> [is_domain_safe] Rejected rule {rule!r} "
                      f"— {pattern!r} unsafe when domain includes zero/negatives")
                return False

    # Trig safety — only reject sin/cos applied directly to a large-range
    # variable. Compositions like sin(A)*cos(A) where A resolves to a small
    # variable are fine and must not be blocked.
    TRIG_FNS = ('sin', 'cos')
    for i, vr in enumerate(valid_ranges):
        vmin, vmax = vr['range']
        if vmax > 1e6:
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
                  max_suggestions=3,
                  base_rules=None,
                  log_path="llm_rule_history.log"):
    """
    High-level wrapper that runs the full LLM suggestion pipeline:
    1. Filter best expressions by length and skeleton diversity
    2. Build prompt — single deduplicated rules list, covered-skeletons block,
       trig-aware instructions, large-range trig warning
    3. Query the LLM at the provided temperature (caller handles escalation)
    4. Parse and validate returned rules (normalised, parenthesis-insensitive
       dedup; all operators_set members accepted as valid tokens)
    5. Filter domain-unsafe rules
    6. Log the full cycle

    Parameters:
    - equation_name (str)
    - current_rules (list[str])
    - best_expressions (list[str]): pre-sorted by reward descending
    - nvars (int)
    - operators_set (set[str])
    - model (str)
    - vars_range (list[dict] | None)
    - temperature (float): caller is responsible for escalation on empty calls
    - max_suggestions (int)
    - base_rules (list[str] | None): shown in the mechanics example only
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

    # 1. Filter best expressions by length and skeleton diversity
    filtered_expressions = filter_best_for_prompt(best_expressions)

    # 2. Build the prompt
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

    # 3. Call the LLM at the temperature the caller decided
    raw = call_openai(prompt, model=model, temperature=temperature)

    # 4. Parse and validate — normalised dedup, all operators_set members allowed
    valid, rejected = parse_and_validate_rules(
        raw,
        existing_rules=current_rules,
        operators_set=operators_set,
        nvars=nvars,
        non_terminal='A'
    )

    # 5. Filter domain-unsafe rules
    if vars_range is not None:
        domain_safe     = [r for r in valid if     is_domain_safe(r, vars_range)]
        domain_rejected = [r for r in valid if not is_domain_safe(r, vars_range)]

        if domain_rejected:
            print(f">>> [suggest_rules] Rejected {len(domain_rejected)} "
                  f"domain-unsafe rule(s): {domain_rejected}")

        rejected += domain_rejected
        valid = domain_safe

    valid = valid[:max_suggestions]

    # 6. Log the full cycle
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