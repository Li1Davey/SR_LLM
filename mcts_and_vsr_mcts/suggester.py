import os
import re
import json
import datetime
from openai import OpenAI

# Initialize OpenAI client using the API key from the environment.
# This keeps secrets out of source control and allows run-time configuration.
def _get_client():
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def build_prompt(equation_name, current_rules, best_expressions, nvars, operators_set, vars_range=None):
    """
    Build a plain-text prompt for LLM to generate new CFG production rules.

    Parameters:
    - equation_name (str): Identifier of the target equation (for context/logging).
    - current_rules (list[str]): Existing production rules, e.g. ['A->(A+A)', 'A->C*X0'].
    - best_expressions (list[str]): Top expressions found so far for context.
    - nvars (int): Number of input variables (X0 .. X{nvars-1}).
    - operators_set (set or list): Allowed operators, e.g. {'sin', 'cos', 'exp'}.
    - vars_range (list[dict], optional): Variable range metadata from the oracle.

    Returns:
    - prompt (str): Assembled prompt to send as the user's message to the LLM.
    """
    
    # STAGE 1 — Variable range summary
    range_lines = []
    transcendental_ok = True  # Initialize as True; will be set to False if conditions dictate

    if vars_range:
        for i, vr in enumerate(vars_range):
            if not isinstance(vr, dict) or 'range' not in vr:
                continue

            lo, hi = vr['range']
            only_pos = vr.get('only_positive', False)
            notes = []

            # Build notes based on the variable's range
            if only_pos:
                notes.append("always positive")
            if hi > 1e6:
                notes.append("very large scale — likely appears in denominator")
            elif hi <= 10:
                notes.append("small scale — may appear raised to higher powers")

            # Set transcendental_ok to False only if all variables are strictly positive
            if only_pos and lo >= 0:
                transcendental_ok = False

            note_str = f" ({', '.join(notes)})" if notes else ""
            range_lines.append(f"  X{i}: [{lo}, {hi}]{note_str}")

    range_block = "Variable ranges:\n" + "\n".join(range_lines) if range_lines else "Variable ranges: (not available)"

    # STAGE 2 — Structural hints derived from best expressions
    has_division = any('/' in e for e in best_expressions)
    has_power = any('**' in e for e in best_expressions)
    has_product = any('*' in e for e in best_expressions)
    has_transcendental = any(func in e for e in best_expressions for func in ['sin', 'cos', 'exp', 'log'])

    # Analyze general complexity and structure
    complexity_check = any(
        isinstance(e, str) and (len(e.split()) > 5 or len(e) > 100)  # Expensive expressions or too many terms
        for e in best_expressions
    )

    hints = []
    if has_division:
        hints.append("- Division is present in some expressions — explore the potential for ratios involving higher powers.")
    if has_power:
        hints.append("- Power terms are prevalent — consider combining powers effectively with other operations.")
    if has_product:
        hints.append("- Products of variables are evident — assess possible combinations that utilize these products.")
    if has_transcendental:
        hints.append("- Transcendental functions are present — inquire about combinations that maintain periodic or exponential behavior.")

    if complexity_check:
        hints.append("- Some expressions are complex; explore simplifying components to create new insights.")
    if not hints:
        hints.append("- No strong structure found yet — consider suggesting a diverse array of algebraic forms, including ratios and powers.")

    hint_block = "\n".join(hints)

    # STAGE 3 — Transcendental function warning
    trig_warning = ""
    if not transcendental_ok and not has_transcendental:
        trig_warning = (
            "\nIMPORTANT: All variables are strictly positive with no indication "
            "of periodic or exponential behavior. Prefer algebraic rules (powers, ratios)."
        )

    # STAGE 4 — Final prompt assembly
    rules_text = "\n".join(current_rules) if current_rules else "(none)"
    best_text = "\n".join(best_expressions) if best_expressions else "(none)"
    ops_text = ", ".join(sorted(list(operators_set))) if operators_set else "(none)"

    prompt = f"""You are helping a symbolic regression system discover a physical equation.
Context:
- Equation: {equation_name}
- {range_block}
- Allowed operators: {ops_text}
- Current production rules:
{rules_text}

Best expressions found so far (sorted by reward, higher is better):
{best_text}

Structural observations:
{hint_block}
{trig_warning}

Task:
Suggest up to 5 new production rules in the exact format:
A-><right-hand-side>

Constraints (strict):
- Every rule must start with 'A->'
- Use only variables X0..X{nvars - 1}, 'C' for constants, and operators from the allowed set.
- Do not repeat existing rules.
- Prefer algebraic structure (powers, ratios) over transcendental functions
  unless the variable ranges clearly support them.
- Output only the rules, one per line, with no additional text.
"""
    return prompt

def call_openai(prompt, model="gpt-4.1-mini", temperature=0.2):
    """
    Send the prompt to OpenAI and return the model's plain text response.

    Parameters:
    - prompt (str): the user prompt (built by build_prompt)
    - model (str): model name to call
    - temperature (float): sampling temperature

    Returns:
    - response_text (str): trimmed text content returned by the model
    """
    client = _get_client()
    # We use the chat completions endpoint with a simple system + user conversation.
    # The system message gives a concise role; the user message contains the prompt.
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that outputs CFG production rules when asked."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
    )

    # Extract the assistant message text; guard against unexpected shapes.
    try:
        text = response.choices[0].message.content
    except Exception:
        # Fallback: convert whole response object to string if structure differs
        text = str(response)

    return text.strip()

def parse_and_validate_rules(response_text, existing_rules, operators_set, nvars, non_terminal='A'):
    """
    Parse the LLM response and return two lists: (valid_rules, rejected_rules).

    Simple, conservative checks:
    - Only accept lines that start with "<non_terminal>->"
    - Reject duplicates already in existing_rules
    - Ensure RHS contains only allowed tokens:
        - variables X0..X{nvars-1}
        - 'C' for constants
        - the non-terminal (e.g., 'A') so recursive rules are possible
        - operators from operators_set (we match by token substring)
        - basic punctuation: + - * / ** ( ) , (comma occasionally used)
    - Trim whitespace and ignore empty lines

    Parameters:
    - response_text (str): raw assistant output (may contain extra text)
    - existing_rules (iterable[str]): rules already present (for duplicate checking)
    - operators_set (set[str]): allowed operator names/tokens, e.g. {'sin', 'cos', '+', '*'}
    - nvars (int): number of variables (X0..X{nvars-1})
    - non_terminal (str): the left-hand non-terminal symbol, default 'A'

    Returns:
    - valid_rules (list[str])
    - rejected_rules (list[str])  # includes malformed or duplicate lines
    """

    # Normalize inputs
    existing = set(existing_rules or [])
    ops = set(operators_set or [])

    # Allowed named tokens: variables, constant placeholder, non-terminal, operator words
    allowed_vars   = {f"X{i}" for i in range(max(0, nvars))}
    allowed_tokens = {"C", non_terminal} | allowed_vars | ops

    # Explicit set of allowed punctuation/operator TOKENS
    # set("+-*/(),**") splits the string into individual characters so '**'
    # is never matched as a two-character token. Using a frozenset literal
    # ensures '**' is treated as a single member.
    ALLOWED_PUNCT = frozenset({"+", "-", "*", "/", "(", ")", ",", "**"})

    valid    = []
    rejected = []

    for raw_line in (response_text or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        # Check 1 — must start with 'A->'
        prefix = f"{non_terminal}->"
        if not line.startswith(prefix):
            rejected.append(line)
            continue

        rhs = line[len(prefix):].strip()

        # Check 2 — RHS must not be empty
        if not rhs:
            rejected.append(line)
            continue

        # Check 3 — deduplicate against the full current grammar
        if line in existing:
            rejected.append(line)
            continue

        # Check 4 — token-level validation
        # Tokenise the RHS: capture '**' before '*' so the two-char token
        # is matched first and not split into two single '*' tokens.
        tokens = re.findall(
            r"\*\*"                          # two-char power operator — must come first
            r"|[A-Za-z_][A-Za-z0-9_]*"      # word tokens: sin, cos, X0, C, A ...
            r"|[0-9]+(?:\.[0-9]+)?"          # numeric literals: 2, 3.14
            r"|[+\-*/(),]",                  # single-char punctuation
            rhs
        )

        malformed = False
        for tok in tokens:
            if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", tok):
                # Inline numeric literal — always allowed
                continue
            if tok in ALLOWED_PUNCT:
                # now correctly matched here as a two-char token
                continue
            if tok in allowed_tokens:
                # Variable, constant, non-terminal, or operator word
                continue
            # Anything else is an unknown token — reject the whole rule
            malformed = True
            break

        if malformed:
            rejected.append(line)
            continue

        valid.append(line)

    return valid, rejected

def is_domain_safe(rule: str, vars_range: list) -> bool:
    """
    Reject rules that use domain-restricted functions
    when variables can be negative or zero.
    """
    if not vars_range:
        return True

    # Filter to only valid dicts — handles character-split or malformed entries
    valid_ranges = [r for r in vars_range if isinstance(r, dict) and 'range' in r]
    if not valid_ranges:
        return True

    # Use valid_ranges everywhere, not the raw vars_range
    has_negatives = any(r['range'][0] < 0 for r in valid_ranges)
    has_zero = any(r['range'][0] <= 0 for r in valid_ranges)

    domain_restricted = ['log', 'sqrt', 'A**0.', 'A**C']

    if has_negatives or has_zero:
        for op in domain_restricted:
            if op in rule:
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
                  log_path="llm_rule_history.log"):
    """
    High-level wrapper that runs the full LLM suggestion pipeline:
    1. Build prompt from current state
    2. Query the LLM
    3. Parse and validate returned rules
    4. Optionally log the request/response and results

    Parameters:
    - equation_name (str)
    - current_rules (list[str])
    - best_expressions (list[str])
    - nvars (int)
    - operators_set (set[str])
    - model (str): model id to call
    - temperature (float): sampling temperature (low for deterministic output)
    - max_suggestions (int): cap how many valid rules to accept from this call
    - log_path (str | None): path to append JSON log entries (optional)

    Returns:
    - valid_rules (list[str]): up to `max_suggestions` validated new rules
    - rejected_rules (list[str]): lines returned by the LLM that were rejected (for inspection)
    """
    
    # Defensive re-parse — only triggers if an entry somehow arrives as a
    # JSON string rather than a dict. Under normal operation (after the
    # mcts_model.py fix) this loop is a no-op since all entries are dicts.
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

    # 1) Build the prompt
    prompt = build_prompt(
        equation_name, 
        current_rules, 
        best_expressions, 
        nvars, 
        operators_set, 
        vars_range=vars_range
    )

    # 2) Call the LLM
    raw = call_openai(prompt, model=model, temperature=temperature)

    # 3) Parse and validate the LLM output
    valid, rejected = parse_and_validate_rules(
        raw, 
        existing_rules=current_rules,
        operators_set=operators_set, 
        nvars=nvars, 
        non_terminal='A'
    )
    
    # 4) Filter out domain-unsafe rules if vars_range was provided
    if vars_range is not None:
        domain_safe     = [r for r in valid if is_domain_safe(r, vars_range)]
        domain_rejected = [r for r in valid if not is_domain_safe(r, vars_range)]

        if domain_rejected:
            print(f">>> [suggest_rules] Rejected {len(domain_rejected)} "
                  f"domain-unsafe rule(s): {domain_rejected}")

        rejected = rejected + domain_rejected
        valid    = domain_safe

    # Enforce max_suggestions
    valid = valid[:max_suggestions]

    # 4) Optional logging: timestamp, inputs, raw response, and results
    if log_path:
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "equation": equation_name,
            "nvars": nvars,
            "operators": sorted(list(operators_set)) if operators_set else [],
            "vars_range": vars_range,
            "current_rules": list(current_rules),
            "best_expressions": list(best_expressions),
            "prompt": prompt,
            "raw_response": raw,
            "valid_rules": valid,
            "rejected_rules": rejected,
            "model": model,
            "temperature": temperature
        }
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception:
            # Keep the function robust: don't raise on logging failures
            pass

    return valid, rejected
