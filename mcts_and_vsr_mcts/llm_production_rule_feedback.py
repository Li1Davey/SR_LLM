import importlib
import json
import os
import re
import time
import uuid
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


# Feature flags and runtime settings for LLM production-rule generation.
ENABLE_PR_FEEDBACK = os.getenv("SCIBENCH_PR_FEEDBACK_ENABLE", "0") == "1"
PR_SUPEXP_FILE = os.getenv("SCIBENCH_SUPEXP_FILE", os.path.join(os.path.dirname(__file__), "supexp.txt"))
PR_MODEL = os.getenv("SCIBENCH_PR_MODEL", os.getenv("SCIBENCH_LLM_MODEL", "gpt-4.1-mini"))
PR_TIMEOUT_SECONDS = float(os.getenv("SCIBENCH_PR_TIMEOUT_SECONDS", "5"))
PR_MAX_OUTPUT_TOKENS = int(os.getenv("SCIBENCH_PR_MAX_OUTPUT_TOKENS", "300"))
PR_TOPK = int(os.getenv("SCIBENCH_PR_TOPK", "8"))
PR_MIN_HOF = int(os.getenv("SCIBENCH_PR_MIN_HOF", "2"))
PR_MIN_HOF_CHANGES = int(os.getenv("SCIBENCH_PR_MIN_HOF_CHANGES", "8"))
PR_MIN_BEST_REWARD = float(os.getenv("SCIBENCH_PR_MIN_BEST_REWARD", "-1e9"))
PR_MIN_REWARD_DELTA = float(os.getenv("SCIBENCH_PR_MIN_REWARD_DELTA", "0.0"))
PR_MAX_CALLS = int(os.getenv("SCIBENCH_PR_MAX_CALLS", "40"))
PR_COOLDOWN_SECONDS = float(os.getenv("SCIBENCH_PR_COOLDOWN_SECONDS", "300"))
PR_MAX_SUGGESTIONS = int(os.getenv("SCIBENCH_PR_MAX_SUGGESTIONS", "6"))
PR_FAILURE_BACKOFF_MAX_MULT = float(os.getenv("SCIBENCH_PR_FAILURE_BACKOFF_MAX_MULT", "8.0"))
PR_RULE_MAX_LEN = int(os.getenv("SCIBENCH_PR_RULE_MAX_LEN", "96"))


@dataclass
class ProductionRuleBank:
    """
    Per-run mutable grammar state backed by a supexp.txt file.

    base_rules:
        Immutable rule set captured at the start of the run.
    current_rules:
        Rules actively known for this run. Starts as base_rules plus any rules
        already present in the run-local supexp file.
    added_rules:
        Only the rules added during this run.
    """

    run_id: str
    supexp_path: str
    base_rules: List[str]
    current_rules: List[str]
    added_rules: List[str] = field(default_factory=list)
    tag: str = ""
    metadata: Dict[str, object] = field(default_factory=dict)

    @property
    def txt_path(self) -> str:
        return self.supexp_path

    def save(self) -> None:
        os.makedirs(os.path.dirname(self.supexp_path) or ".", exist_ok=True)
        existing_rhs = set(_iter_existing_rhs(self.supexp_path))

        with open(self.supexp_path, "a") as f:
            for rule in self.added_rules:
                rhs = _rule_to_rhs(rule)
                if rhs and rhs not in existing_rhs:
                    f.write(rhs + "\n")
                    existing_rhs.add(rhs)

    def append_unique(self, rules: Iterable[str]) -> int:
        added = 0
        existing = set(self.current_rules)

        for rule in rules:
            normalized = _normalize_rule(rule)
            if not normalized or normalized in existing:
                continue
            self.current_rules.append(normalized)
            self.added_rules.append(normalized)
            existing.add(normalized)
            added += 1

        if added:
            self.save()
        return added


# Internal state for throttling/deduplication.
_LAST_PUSH_TS = 0.0
_LAST_PUSH_BEST_REWARD = float("-inf")
_LAST_PROMPT_FINGERPRINT = ""
_CALL_COUNT = 0
_FAIL_STREAK = 0
_HOF_CHANGE_COUNTER = 0


def _log_skip(message: str) -> int:
    print(f"[PR_FEEDBACK] {message}", flush=True)
    return 0


def _normalize_rule(rule: str) -> str:
    if rule is None:
        return ""
    text = str(rule).strip()
    text = text.strip("`")
    return re.sub(r"\s+", "", text)


def _rule_to_rhs(rule: str) -> str:
    text = _normalize_rule(rule)
    if not text:
        return ""
    return text.split("->", 1)[1].strip() if "->" in text else text.strip()


def _iter_existing_rhs(supexp_path: str) -> Iterable[str]:
    if not os.path.exists(supexp_path):
        return []

    rhs_lines: List[str] = []
    with open(supexp_path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            rhs = _rule_to_rhs(line)
            if rhs:
                rhs_lines.append(rhs)
    return rhs_lines


def _slugify(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(text).strip())
    text = text.strip("-._")
    return text or "run"


def _current_cooldown_seconds() -> float:
    mult = min(PR_FAILURE_BACKOFF_MAX_MULT, 2 ** _FAIL_STREAK)
    return PR_COOLDOWN_SECONDS * mult


def create_run_rule_bank(
    base_rules: Sequence[str],
    tag: str = "",
    runs_dir: Optional[str] = None,
    run_id: Optional[str] = None,
    extra_metadata: Optional[Dict[str, object]] = None,
) -> ProductionRuleBank:
    """
    Create per-run mutable grammar state backed by a run-local supexp.txt file.

    The shared/base grammar remains unchanged; newly accepted rules are appended
    to the current run's supexp.txt for later loading.

    runs_dir is kept for backward compatibility and is currently unused because
    the active flow is keyed off SCIBENCH_SUPEXP_FILE.
    """
    _ = runs_dir  # backward-compatible unused parameter
    supexp_path = os.getenv("SCIBENCH_SUPEXP_FILE", PR_SUPEXP_FILE)
    current_rules = [_normalize_rule(x) for x in base_rules if _normalize_rule(x)]

    for rhs in _iter_existing_rhs(supexp_path):
        rule = _normalize_rule(f"A->{rhs}")
        if rule and rule not in current_rules:
            current_rules.append(rule)

    return ProductionRuleBank(
        run_id=run_id or f"{time.strftime('%Y%m%d-%H%M%S')}-{_slugify(tag) if tag else 'run'}-{uuid.uuid4().hex[:8]}",
        supexp_path=supexp_path,
        base_rules=[_normalize_rule(x) for x in base_rules if _normalize_rule(x)],
        current_rules=current_rules,
        added_rules=[],
        tag=tag,
        metadata=extra_metadata.copy() if extra_metadata else {},
    )


def load_run_rule_bank(json_path: str) -> ProductionRuleBank:
    raise NotImplementedError(
        "load_run_rule_bank is not used in the supexp-backed flow "
        f"(got {json_path!r})"
    )


def maybe_generate_production_rules(
    hall_of_fame: Sequence[Tuple[str, float, str]],
    rule_bank: ProductionRuleBank,
    nvars: int,
    operators_set: Optional[Sequence[str]] = None,
    non_terminal_node: str = "A",
    force: bool = False,
) -> int:
    """
    Ask an OpenAI model for new abstract production rules and append accepted
    rules to the current run's mutable rule bank.

    Returns the number of new rules appended to this run.
    """
    global _LAST_PUSH_TS, _LAST_PUSH_BEST_REWARD, _LAST_PROMPT_FINGERPRINT
    global _CALL_COUNT, _FAIL_STREAK, _HOF_CHANGE_COUNTER

    if not ENABLE_PR_FEEDBACK:
        return _log_skip("disabled")
    if not hall_of_fame or len(hall_of_fame) < PR_MIN_HOF:
        size = 0 if not hall_of_fame else len(hall_of_fame)
        return _log_skip(f"skipped: hall_of_fame too small ({size})")
    if _CALL_COUNT >= PR_MAX_CALLS:
        return _log_skip("skipped: max calls reached")

    _HOF_CHANGE_COUNTER += 1
    if (not force) and _HOF_CHANGE_COUNTER < PR_MIN_HOF_CHANGES:
        return _log_skip(
            f"skipped: hof change counter {_HOF_CHANGE_COUNTER}/{PR_MIN_HOF_CHANGES}"
        )

    try:
        best_reward = max(float(x[1]) for x in hall_of_fame)
    except Exception:
        best_reward = float("-inf")

    if best_reward < PR_MIN_BEST_REWARD:
        return _log_skip(f"skipped: best_reward {best_reward} < {PR_MIN_BEST_REWARD}")
    if (not force) and (best_reward - _LAST_PUSH_BEST_REWARD) < PR_MIN_REWARD_DELTA:
        return _log_skip(
            f"skipped: reward delta too small ({best_reward - _LAST_PUSH_BEST_REWARD})"
        )

    fingerprint = _hof_fingerprint(hall_of_fame, PR_TOPK)
    if (not force) and fingerprint == _LAST_PROMPT_FINGERPRINT:
        return 0

    if (not force) and (time.time() - _LAST_PUSH_TS) < _current_cooldown_seconds():
        return 0

    if not os.getenv("OPENAI_API_KEY", "").strip():
        return _log_skip("skipped: OPENAI_API_KEY missing")

    allowed_ops = _allowed_ops_for_prompt(operators_set)
    prompt = _build_prompt(
        hall_of_fame=hall_of_fame,
        current_rules=rule_bank.current_rules,
        allowed_ops=allowed_ops,
        nvars=nvars,
        non_terminal_node=non_terminal_node,
    )

    try:
        openai_module = importlib.import_module("openai")
        client = openai_module.OpenAI()
        t0 = time.time()
        response = client.responses.create(
            model=PR_MODEL,
            input=prompt,
            max_output_tokens=PR_MAX_OUTPUT_TOKENS,
            timeout=PR_TIMEOUT_SECONDS,
        )
        raw = getattr(response, "output_text", "")
        print(f"[PR_FEEDBACK] LLM call completed in {time.time() - t0:.2f}s", flush=True)
        _CALL_COUNT += 1
        _FAIL_STREAK = 0
        _HOF_CHANGE_COUNTER = 0
    except Exception as e:
        _LAST_PUSH_TS = time.time()
        _CALL_COUNT += 1
        _FAIL_STREAK += 1
        _HOF_CHANGE_COUNTER = 0
        print(f"[PR_FEEDBACK] generation request failed: {e}", flush=True)
        return 0

    suggestions = _parse_json_or_lines(raw, key="production_rules")
    accepted: List[str] = []
    seen = set(rule_bank.current_rules)

    for rule in suggestions:
        clean = _sanitize_rule(
            rule,
            current_rules=rule_bank.current_rules,
            allowed_ops=allowed_ops,
            non_terminal_node=non_terminal_node,
        )
        if not clean or clean in seen:
            continue
        accepted.append(clean)
        seen.add(clean)
        if len(accepted) >= PR_MAX_SUGGESTIONS:
            break

    if not accepted:
        for rule in _heuristic_rule_fallback(allowed_ops, non_terminal_node=non_terminal_node):
            clean = _sanitize_rule(
                rule,
                current_rules=rule_bank.current_rules,
                allowed_ops=allowed_ops,
                non_terminal_node=non_terminal_node,
            )
            if not clean or clean in seen:
                continue
            accepted.append(clean)
            seen.add(clean)
            if len(accepted) >= PR_MAX_SUGGESTIONS:
                break

    added = rule_bank.append_unique(accepted)
    _LAST_PUSH_TS = time.time()
    _LAST_PUSH_BEST_REWARD = best_reward
    _LAST_PROMPT_FINGERPRINT = fingerprint

    if added > 0:
        print(f"[PR_FEEDBACK] added {added} rule(s) to {rule_bank.txt_path}", flush=True)
    else:
        print("[PR_FEEDBACK] no new production rules accepted", flush=True)
    return added


def _canonicalize_eq_structure(eq: str) -> str:
    if eq is None:
        return ""
    text = re.sub(r"\s+", "", str(eq))

    number_pat = r"(?<![A-Za-z_])[-+]?(?:\d+\.\d*|\d*\.\d+|\d+)(?:e[-+]?\d+)?"

    def repl(match):
        token = match.group(0)
        try:
            value = float(token)
        except Exception:
            return token
        if abs(value) < 1e-12:
            return "0"
        if abs(value - 1.0) < 1e-12:
            return "1"
        if abs(value + 1.0) < 1e-12:
            return "-1"
        return "CNUM"

    return re.sub(number_pat, repl, text)


def _structure_features(eq: str) -> Dict[str, object]:
    text = str(eq)
    return {
        "has_div": "/" in text,
        "has_exp": "exp(" in text,
        "has_log": "log(" in text,
        "has_sub": "-" in text,
        "has_mul": "*" in text,
        "has_sin": "sin(" in text,
        "has_cos": "cos(" in text,
        "depth_hint": text.count("("),
        "structure_key": _canonicalize_eq_structure(text),
    }


def _select_diverse_panel(
    candidates: Sequence[Tuple[str, float, str]],
    panel_size: int,
) -> List[Tuple[str, float, str]]:
    if not candidates:
        return []

    scored = sorted(candidates, key=lambda x: float(x[1]), reverse=True)
    panel: List[Tuple[str, float, str]] = []
    seen = set()

    def try_add(item) -> bool:
        key = _canonicalize_eq_structure(item[2])
        if key in seen:
            return False
        seen.add(key)
        panel.append(item)
        return True

    for item in scored:
        try_add(item)
        if len(panel) >= max(2, panel_size // 2):
            break

    rich = sorted(
        scored,
        key=lambda x: (
            int(_structure_features(x[2])["has_div"])
            + int(_structure_features(x[2])["has_exp"])
            + int(_structure_features(x[2])["has_log"])
            + int(_structure_features(x[2])["has_sub"])
            + int(_structure_features(x[2])["has_mul"]),
            int(_structure_features(x[2])["depth_hint"]),
            float(x[1]),
        ),
        reverse=True,
    )
    for item in rich:
        try_add(item)
        if len(panel) >= panel_size:
            break

    if len(panel) < panel_size:
        for item in scored:
            try_add(item)
            if len(panel) >= panel_size:
                break

    return panel[:panel_size]


def _hof_fingerprint(candidates: Sequence[Tuple[str, float, str]], topk: int) -> str:
    parts = []
    for _, reward, eq in _select_diverse_panel(candidates, topk):
        parts.append(f"{round(float(reward), 6)}::{_canonicalize_eq_structure(eq)}")
    return "|".join(parts)


def _truncate_eq_for_prompt(eq: str, max_len: int = 220) -> str:
    if not eq:
        return ""
    text = str(eq).replace("\n", " ").strip()
    return text if len(text) <= max_len else (text[:max_len] + " ...")


def _allowed_ops_for_prompt(operators_set: Optional[Sequence[str]]) -> List[str]:
    ops = {str(x) for x in (operators_set or [])}
    allowed = ["+", "-", "*", "/", "(", ")"]
    if "exp" in ops:
        allowed.append("exp")
    if "log" in ops:
        allowed.append("log")
    if "sin" in ops:
        allowed.append("sin")
    if "cos" in ops:
        allowed.append("cos")
    if "sqrt" in ops:
        allowed.append("sqrt")
    if "abs" in ops:
        allowed.append("abs")
    return allowed


def _build_prompt(
    hall_of_fame: Sequence[Tuple[str, float, str]],
    current_rules: Sequence[str],
    allowed_ops: Sequence[str],
    nvars: int,
    non_terminal_node: str,
) -> str:
    panel = _select_diverse_panel(hall_of_fame, PR_TOPK)
    panel_lines = []

    for _, reward, eq in panel:
        feat = _structure_features(eq)
        tags = []
        for tag_name, field_name in [
            ("div", "has_div"),
            ("exp", "has_exp"),
            ("log", "has_log"),
            ("sub", "has_sub"),
            ("mul", "has_mul"),
            ("sin", "has_sin"),
            ("cos", "has_cos"),
        ]:
            if feat[field_name]:
                tags.append(tag_name)
        panel_lines.append(
            f"reward={float(reward):.6f} | tags={','.join(tags) if tags else 'plain'} | "
            f"eq={_truncate_eq_for_prompt(eq)}"
        )

    existing_preview = "\n".join(f"- {rule}" for rule in list(current_rules)[:50])
    allowed_ops_text = ", ".join(allowed_ops)

    return (
        "You are proposing new grammar production rules for symbolic regression.\n"
        "The engine already has a base grammar, and this run may append a few NEW abstract rules.\n"
        "Propose compact, reusable rules that are likely to help express patterns found in the current hall of fame.\n\n"
        "Return STRICT JSON only:\n"
        "{\"production_rules\": [\"A->...\", \"A->...\"]}\n\n"
        f"Hard constraints:\n"
        f"- Every rule must start with '{non_terminal_node}->'.\n"
        "- Use only abstract placeholders A and C on the RHS.\n"
        "- Do NOT use X0, X1, or any Xi variable names.\n"
        "- Do NOT use B, K, k_shared, numeric literals, or target-specific constants.\n"
        f"- Use only these operators/functions: {allowed_ops_text}.\n"
        f"- Keep each full rule <= {PR_RULE_MAX_LEN} characters.\n"
        "- Prefer reusable motifs involving cancellation, repeated transformed terms, symmetries, ratios, or compositions.\n"
        "- Avoid trivial rewrites like A->A, A->C, A->(A+A), or copies of existing rules.\n"
        "- Provide 3 to 8 suggestions.\n\n"
        "Examples of acceptable style:\n"
        f"- {non_terminal_node}->(A-A)/(A-A)\n"
        f"- {non_terminal_node}->A*exp(A-A)\n"
        f"- {non_terminal_node}->1-(A-A)/(A-A)\n"
        f"- {non_terminal_node}->(A*exp(A)-A*exp(A))/(A-A)\n\n"
        "Existing rules for this run (do not repeat them):\n"
        f"{existing_preview}\n\n"
        f"Context: current equation family uses up to {nvars} variables, but your new rules must stay abstract.\n\n"
        "Hall-of-fame panel:\n"
        + "\n".join(panel_lines)
    )


def _parse_json_or_lines(raw_text: str, key: str) -> List[str]:
    text = (raw_text or "").strip()
    if not text:
        return []

    if text.startswith("{"):
        try:
            payload = json.loads(text)
            items = payload.get(key, []) if isinstance(payload, dict) else []
            if isinstance(items, list):
                return [str(x).strip() for x in items if str(x).strip()]
        except Exception:
            pass

    lines = []
    for line in text.splitlines():
        cleaned = line.strip().lstrip("- ").strip()
        if cleaned:
            lines.append(cleaned)
    return lines


def _sanitize_rule(
    rule: str,
    current_rules: Sequence[str],
    allowed_ops: Sequence[str],
    non_terminal_node: str = "A",
) -> str:
    text = _normalize_rule(rule)
    if not text:
        return ""

    if ":" in text and "->" not in text:
        return ""
    if "->" not in text:
        text = f"{non_terminal_node}->{text}"

    lhs, rhs = text.split("->", 1)
    if lhs != non_terminal_node or not rhs:
        return ""

    if len(text) > PR_RULE_MAX_LEN:
        return ""
    if text in current_rules:
        return ""
    if re.search(r"X\d+", rhs):
        return ""
    if any(tok in rhs for tok in ["B", "K", "k_shared"]):
        return ""
    if re.search(r"(?<![A-Za-z_])\d+(?:\.\d+)?", rhs):
        stripped_numbers = re.sub(r"(?<![A-Za-z_])1(?![A-Za-z_])", "", rhs)
        if re.search(r"(?<![A-Za-z_])\d+(?:\.\d+)?", stripped_numbers):
            return ""

    if not re.fullmatch(r"[A-Za-z0-9_+\-*/().]+", rhs):
        return ""

    if rhs.count("A") < 1:
        return ""
    if rhs.count("exp(") > 2 or rhs.count("/") > 2:
        return ""

    banned_exact_rhs = {
        "A",
        "C",
        "(A+A)",
        "(A-A)",
        "A*A",
        "(A)/(A)",
        "exp(A)",
        "log(A)",
        "sin(A)",
        "cos(A)",
        "sqrt(A)",
        "abs(A)",
    }
    if rhs in banned_exact_rhs:
        return ""

    used_funcs = set(re.findall(r"([A-Za-z_]+)\(", rhs))
    allowed_func_names = {x for x in allowed_ops if x.isalpha()}
    if any(func not in allowed_func_names for func in used_funcs):
        return ""

    return f"{non_terminal_node}->{rhs}"


def _heuristic_rule_fallback(
    allowed_ops: Sequence[str],
    non_terminal_node: str = "A",
) -> List[str]:
    funcs = {x for x in allowed_ops if x.isalpha()}
    out = [
        f"{non_terminal_node}->(A-A)/(A-A)",
        f"{non_terminal_node}->1-(A-A)/(A-A)",
    ]
    if "exp" in funcs:
        out.extend(
            [
                f"{non_terminal_node}->A*exp(A-A)",
                f"{non_terminal_node}->(A*exp(A)-A*exp(A))/(A-A)",
            ]
        )
    if "log" in funcs:
        out.append(f"{non_terminal_node}->(A-A)*log(A)")
    if "sin" in funcs:
        out.append(f"{non_terminal_node}->(A-A)*sin(A)")
    if "cos" in funcs:
        out.append(f"{non_terminal_node}->(A-A)*cos(A)")
    if "sqrt" in funcs:
        out.append(f"{non_terminal_node}->sqrt((A-A)*(A-A))")
    return out


if __name__ == "__main__":
    demo_base = [
        "A->(A+A)",
        "A->(A-A)",
        "A->A*A",
        "A->(A)/(A)",
        "A->exp(A)",
        "A->C",
        "A->C*X0",
        "A->C*X1",
    ]
    bank = create_run_rule_bank(demo_base, tag="demo")
    print(bank.run_id)
    print(bank.txt_path)
