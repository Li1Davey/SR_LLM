import json
from suggester import (
    filter_best_for_prompt,
    build_prompt,
    call_openai,
    parse_and_validate_rules,
    is_domain_safe,
)

# ── Shared test config ─────────────────────────────────────────────────────────
equation_name = "SymbolicDiscovery"
nvars         = 2
operators_set = {"*", "**", "+", "-", "/", "cos", "exp", "log", "sin"}

vars_range = [
    {"name": "Uniform", "range": [0.1,  10.0], "dim": [1], "only_positive": True},
    {"name": "Uniform", "range": [1e10, 1e12], "dim": [1], "only_positive": True},
]

base_rules = [
    "A->(A+A)", "A->(A-A)", "A->A*A", "A->(A)/(A)",
    "A->exp(A)", "A->log(A)", "A->sin(A)", "A->cos(A)",
    "A->C*X0", "A->C*X1", "A->C",
]

best_expressions = [
    "10622252.49805161*X0**7/X1 + 511887101607.172*X0**3/X1",
    "17.404949221259727*X0**2 - 37.39311110752837*X0",
    "X0**2/(32.901848814455136*X0 - 412.6148738667983) - 14546.45732663363*X0/(32.901848814455136*X0 - 412.6148738667983)",
    "141.6923314941164*X0 - 324.2944591439409",
    "89.9605354596868*X0",
    "3.141592653589793*X0**2/X1 + 2.718281828459045*X0/X1",
    "7.389056098930650*X0**3/X1 - 1.4142135623730951*X0**2/X1",
    "0.5*X0**4/X1 + 12.566370614359172*X0**2/X1",
    "X0**5/(X1 + 3.141592653589793*X0**2)",
    "6.283185307179586*X0**3/(X1 - 1000000000.0*X0)",
    "X0**2/(X1*0.000000001 + X0) + 4.71238898038469*X0/X1",
    "9.869604401089358*X0**6/X1 + 0.3183098861837907*X0**4/X1",
    "X0**3/(X1 + X0**2) - 2.0*X0**2/X1",
    "1.7724538509055159*X0**5/X1 + 0.8862269254527580*X0**3/X1",
    "X0**4/(2.0*X1) + X0**2/(4.0*X1)",
    "0.001*X0**8/X1 - 0.0001*X0**6/X1",
    "X0**2*log(X0)/X1 + 3.0*X0/X1",
    "X0**3*log(X0)/X1 - X0**2*log(X0)/X1",
    "exp(X0)*X0/X1 + exp(X0)*X0**2/X1",
    "X0**2/(X1*(log(X0) + 1.0)) + X0**3/(X1*(log(X0) + 2.0))",
]

max_suggestions = 10

# ── Step 1: filter_best_for_prompt ────────────────────────────────────────────
print("=" * 60)
print("STEP 1 — filter_best_for_prompt")
print("=" * 60)
filtered = filter_best_for_prompt(best_expressions)
print(f"  Input : {len(best_expressions)} expressions")
print(f"  Output: {len(filtered)} kept (max_expr_len=120, max_show=15)")
for e in filtered:
    print(f"    [{len(e):3d} chars]  {e}")

# ── Step 2: build_prompt ──────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2 — build_prompt")
print("=" * 60)
prompt = build_prompt(
    equation_name=equation_name,
    current_rules=base_rules,
    best_expressions=filtered,
    nvars=nvars,
    operators_set=operators_set,
    vars_range=vars_range,
    max_suggestions=max_suggestions,
    base_rules=base_rules,
)
print(prompt)

# ── Step 3: call_openai ───────────────────────────────────────────────────────
print("=" * 60)
print("STEP 3 — call_openai (live)")
print("=" * 60)
raw = call_openai(prompt, model="gpt-4.1-mini")
print("  Raw LLM response:")
print(raw)

# ── Step 4: parse_and_validate_rules ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 4 — parse_and_validate_rules")
print("=" * 60)
valid, rejected = parse_and_validate_rules(
    raw,
    existing_rules=base_rules,
    operators_set=operators_set,
    nvars=nvars,
    non_terminal='A',
)
print(f"  Valid    ({len(valid)}):    {valid}")
print(f"  Rejected ({len(rejected)}): {rejected}")

# ── Step 5: is_domain_safe ────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 5 — is_domain_safe")
print("=" * 60)
domain_safe     = [r for r in valid if     is_domain_safe(r, vars_range)]
domain_rejected = [r for r in valid if not is_domain_safe(r, vars_range)]
print(f"  Safe     ({len(domain_safe)}):     {domain_safe}")
print(f"  Rejected ({len(domain_rejected)}): {domain_rejected}")