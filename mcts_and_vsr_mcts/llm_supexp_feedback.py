import importlib
import json
import os
import re
import time
from typing import Iterable, List, Sequence, Tuple


ENABLE_SUPEXP = os.getenv("SCIBENCH_SUPEXP_ENABLE", "0") == "1"
SUPEXP_FILE = os.getenv("SCIBENCH_SUPEXP_FILE", os.path.join(os.path.dirname(__file__), "supexp.txt"))
SUPEXP_AUTO_APPEND = os.getenv("SCIBENCH_SUPEXP_AUTO_APPEND", "0") == "1"
SUPEXP_TOPK = int(os.getenv("SCIBENCH_SUPEXP_TOPK", "8"))
SUPEXP_COOLDOWN_SECONDS = float(os.getenv("SCIBENCH_SUPEXP_COOLDOWN_SECONDS", "120"))
SUPEXP_MODEL = os.getenv("SCIBENCH_SUPEXP_MODEL", os.getenv("SCIBENCH_LLM_MODEL", "gpt-4.1-mini"))
SUPEXP_TIMEOUT_SECONDS = float(os.getenv("SCIBENCH_SUPEXP_TIMEOUT_SECONDS", "20"))
SUPEXP_MAX_OUTPUT_TOKENS = int(os.getenv("SCIBENCH_SUPEXP_MAX_OUTPUT_TOKENS", "256"))
SUPEXP_MAX_SUGGESTIONS = int(os.getenv("SCIBENCH_SUPEXP_MAX_SUGGESTIONS", "12"))
SUPEXP_MIN_HOF = int(os.getenv("SCIBENCH_SUPEXP_MIN_HOF", "2"))
SUPEXP_MIN_BEST_REWARD = float(os.getenv("SCIBENCH_SUPEXP_MIN_BEST_REWARD", "0.5"))
SUPEXP_MIN_REWARD_DELTA = float(os.getenv("SCIBENCH_SUPEXP_MIN_REWARD_DELTA", "0.05"))
SUPEXP_MAX_CALLS = int(os.getenv("SCIBENCH_SUPEXP_MAX_CALLS", "40"))
SUPEXP_FAILURE_BACKOFF_MAX_MULT = float(os.getenv("SCIBENCH_SUPEXP_FAILURE_BACKOFF_MAX_MULT", "8.0"))
SUPEXP_MIN_HOF_CHANGES = int(os.getenv("SCIBENCH_SUPEXP_MIN_HOF_CHANGES", "4"))
SUPEXP_PREFER_HEURISTICS_FIRST = os.getenv("SCIBENCH_SUPEXP_PREFER_HEURISTICS_FIRST", "1") == "1"
SUPEXP_REQUIRE_APPEND_GAIN = int(os.getenv("SCIBENCH_SUPEXP_REQUIRE_APPEND_GAIN", "1"))

_LAST_PUSH_TS = 0.0
_LAST_PUSH_BEST_REWARD = float("-inf")
_LAST_PROMPT_FINGERPRINT = ""
_CALL_COUNT = 0
_FAIL_STREAK = 0
_HOF_CHANGE_COUNTER = 0


def _is_trivial_atom(s: str) -> bool:
    t = s.replace(" ", "")
    trivial = {
        "X0", "X1", "X0/X1", "X1/X0", "(X0+X1)", "(X0-X1)", "(X1-X0)",
        "exp(X0)", "exp(X1)", "log(X0)", "log(X1)", "sin(X0)", "sin(X1)", "cos(X0)", "cos(X1)",
    }
    if t in trivial:
        return True
    if re.fullmatch(r"[+-]?\d*\.?\d+\*?X\d+", t):
        return True
    return False

def _looks_like_numeric_guard_hack(s: str) -> bool:
    """
    Reject atoms that are really just numerical stabilizers rather than
    transferable symbolic structure.
    """
    t = s.replace(" ", "")

    # Explicit epsilon literals.
    if re.search(r"1e-\d+", t):
        return True

    # Tiny decimal literals often used as denominator guards.
    if re.search(r"0\.0{3,}\d+", t):
        return True

    # Common shifted-difference patterns.
    if "(X1-X0)+" in t or "(X0-X1)+" in t:
        return True
    if "(X1-X0)-" in t or "(X0-X1)-" in t:
        return True

    return False

def _hof_fingerprint(candidates: Sequence[Tuple[str, float, str]], topk: int) -> str:
    top = sorted(candidates, key=lambda x: x[1], reverse=True)[:topk]
    parts = []
    for _, reward, eq in top:
        parts.append(f"{round(float(reward), 6)}::{_truncate_eq_for_prompt(eq, max_len=160)}")
    return "|".join(parts)


def _current_cooldown_seconds() -> float:
    mult = min(SUPEXP_FAILURE_BACKOFF_MAX_MULT, 2 ** _FAIL_STREAK)
    return SUPEXP_COOLDOWN_SECONDS * mult

def _heuristic_atoms_from_hof(candidates: Sequence[Tuple[str, float, str]], nvars: int) -> List[str]:
    """Extract reusable parameterized atoms from top HoF strings when LLM output is empty/noisy."""
    top = sorted(candidates, key=lambda x: x[1], reverse=True)[:SUPEXP_TOPK]
    out = []
    for _, _, eq in top:
        s = str(eq)

        # exp(-a/Xi)  -> exp(-K/Xi)
        for m in re.finditer(r"exp\(\s*([-+]?\d*\.?\d+(?:e[-+]?\d+)?)\s*/\s*(X\d+)\s*\)", s):
            var = m.group(2)
            if int(var[1:]) < nvars:
                out.append(f"exp(-K/{var})")

        # Xi / (Xi + a)  -> Xi/(Xi + K)
        pat1 = r"(X\d+)\s*/\s*\(\s*(?:1\.0\*)?\1\s*[+\-]\s*[-+]?\d*\.?\d+(?:e[-+]?\d+)?\s*\)"
        for m in re.finditer(pat1, s):
            var = m.group(1)
            if int(var[1:]) < nvars:
                out.append(f"{var}/({var} + K)")

    # keep order, dedupe
    uniq = []
    seen = set()
    for a in out:
        if a in seen:
            continue
        seen.add(a)
        uniq.append(a)
    return uniq

def _truncate_eq_for_prompt(eq: str, max_len: int = 220) -> str:
    if not eq:
        return ""
    s = str(eq).replace("\n", " ").strip()
    if len(s) <= max_len:
        return s
    return s[:max_len] + " ..."


def _parse_json_or_lines(raw_text: str) -> List[str]:
    txt = (raw_text or "").strip()
    if not txt:
        return []

    if txt.startswith("{"):
        try:
            payload = json.loads(txt)
            exps = payload.get("subexpressions", []) if isinstance(payload, dict) else []
            if isinstance(exps, list):
                return [str(x).strip() for x in exps if str(x).strip()]
        except Exception:
            pass

    out = []
    for line in txt.splitlines():
        s = line.strip().lstrip("- ").strip()
        if s:
            out.append(s)
    return out


def _sanitize_subexpression(expr: str, nvars: int) -> str:
    s = (expr or "").strip()
    if not s:
        return ""

    # Very conservative charset.
    if not re.fullmatch(r"[A-Za-z0-9_+\-*/().,\s]+", s):
        return ""

    # Strip optional LHS if model returns grammar-rule-like text.
    if "->" in s:
        s = s.split("->", 1)[1].strip()

    # Remove markdown wrappers
    if s.startswith("`") and s.endswith("`"):
        s = s.strip("`").strip()

    # Variable bounds check
    for m in re.findall(r"X(\d+)", s):
        if int(m) >= nvars:
            return ""

    # Must contain at least one variable or placeholder and some structure.
    if not any(tok in s for tok in ["X", "C", "K", "exp(", "log(", "sin(", "cos(", "/", "*"]):
        return ""

    if _is_trivial_atom(s):
        return ""

    if _looks_like_numeric_guard_hack(s):
        return ""

    # Conservative complexity limits
    if len(s) > 64:
        return ""
    if s.count("exp(") > 1:
        return ""
    if s.count("**") > 2:
        return ""
    if s.count("/") > 2:
        return ""
    if any(tok in s for tok in ["zoo", "oo", "nan"]):
        return ""

    # Avoid plain single-variable forms without transferability.
    has_placeholder = ("C" in s) or ("K" in s)
    has_binary = any(op in s for op in ["+", "-", "*", "/"])
    if not has_placeholder and not has_binary:
        return ""

    return s

def _ensure_supexp_file(path: str) -> None:
    if not path:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("# auto-generated supexp suggestions will be appended below\n")


def _read_existing_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            out.append(s)
    return out


def _append_unique_lines(path: str, lines: Iterable[str]) -> int:
    uniq_new = [x.strip() for x in lines if x and x.strip()]
    if not uniq_new:
        return 0

    existing = set(_read_existing_lines(path))
    to_add = [x for x in uniq_new if x not in existing]
    if not to_add:
        return 0

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        if os.path.getsize(path) > 0:
            f.write("\n")
        for x in to_add:
            f.write(x + "\n")
    return len(to_add)


def _build_prompt(candidates: Sequence[Tuple[str, float, str]], nvars: int) -> str:
    top = sorted(candidates, key=lambda x: x[1], reverse=True)[:SUPEXP_TOPK]
    cand_lines = []
    for _, reward, eq in top:
        cand_lines.append(f"reward={reward:.6f} | eq={_truncate_eq_for_prompt(eq)}")

    return (
        "You are helping symbolic-regression grammar discovery.\n"
        "Given high-reward expressions, propose compact reusable subexpressions\n"
        "that are likely to transfer across equations.\n\n"
        "Return STRICT JSON only:\n"
        "{\"subexpressions\": [\"...\", \"...\"]}\n\n"
        "Hard constraints for each candidate:\n"
        f"- Variables must be among X0..X{max(nvars-1,0)} only.\n"
        "- RHS only (NO 'A->' prefix).\n"
        "- Use only functions/operators already in candidate equations: + - * / exp log sin cos and parentheses.\n"
        "- Keep each candidate <= 64 chars.\n"
        "- Keep each candidate shallow: <=1 exp(...), <=2 '/' and <=2 '**'.\n"
        "- Prefer patterns with placeholders C or K for transferability.\n"
        "- Avoid trivial atoms like X0, X1, X0/X1, exp(X0), sin(X0), cos(X1).\n"
        "- Do NOT output numerical guard hacks like '+1e-8', '(X1-X0)+1e-8', or denominator shifts.\n"
        "- Avoid constants-only expressions and avoid duplicates/near-duplicates.\n"
        "- Provide 4 to 10 suggestions.\n\n"
        "Bad examples (DO NOT output):\n"
        "- zoo*X0\n"
        "- exp(exp(X0))\n"
        "- (X1-X0)+1e-8\n"
        "- extremely long nested forms\n\n"
        "Candidates:\n" + "\n".join(cand_lines)
    )


def maybe_generate_supexpressions(hall_of_fame: Sequence[Tuple[str, float, str]], nvars: int) -> int:
    global _LAST_PUSH_TS, _LAST_PUSH_BEST_REWARD, _LAST_PROMPT_FINGERPRINT, _CALL_COUNT, _FAIL_STREAK, _HOF_CHANGE_COUNTER

    if not ENABLE_SUPEXP:
        return 0
    if not hall_of_fame:
        return 0
    if len(hall_of_fame) < SUPEXP_MIN_HOF:
        return 0

    _HOF_CHANGE_COUNTER += 1
    if _HOF_CHANGE_COUNTER < SUPEXP_MIN_HOF_CHANGES:
        return 0
    if _CALL_COUNT >= SUPEXP_MAX_CALLS:
        return 0

    try:
        best_reward = max(float(x[1]) for x in hall_of_fame)
    except Exception:
        best_reward = float("-inf")

    if best_reward < SUPEXP_MIN_BEST_REWARD:
        return 0
    if (best_reward - _LAST_PUSH_BEST_REWARD) < SUPEXP_MIN_REWARD_DELTA:
        return 0

    fp = _hof_fingerprint(hall_of_fame, SUPEXP_TOPK)
    if fp == _LAST_PROMPT_FINGERPRINT:
        return 0

    cooldown_s = _current_cooldown_seconds()
    if (time.time() - _LAST_PUSH_TS) < cooldown_s:
        return 0

    if SUPEXP_AUTO_APPEND:
        try:
            _ensure_supexp_file(SUPEXP_FILE)
        except Exception as e:
            print(f"[SUPEXP] could not initialize file {SUPEXP_FILE}: {e}", flush=True)

    seen = set()
    cleaned = []

    # New behavior: try heuristics first to avoid blocking the MCTS hot path
    if SUPEXP_PREFER_HEURISTICS_FIRST:
        for a in _heuristic_atoms_from_hof(hall_of_fame, nvars):
            s = _sanitize_subexpression(a, nvars)
            if not s or s in seen:
                continue
            cleaned.append(s)
            seen.add(s)
            if len(cleaned) >= SUPEXP_MAX_SUGGESTIONS:
                break

        if cleaned and not SUPEXP_AUTO_APPEND:
            print(f"[SUPEXP] heuristic suggestions ready ({len(cleaned)}), auto-append disabled", flush=True)
            _LAST_PUSH_TS = time.time()
            _LAST_PUSH_BEST_REWARD = best_reward
            _LAST_PROMPT_FINGERPRINT = fp
            _HOF_CHANGE_COUNTER = 0
            return 0

        if cleaned and SUPEXP_REQUIRE_APPEND_GAIN:
            added = _append_unique_lines(SUPEXP_FILE, cleaned) if SUPEXP_AUTO_APPEND else 0
            _LAST_PUSH_TS = time.time()
            _LAST_PUSH_BEST_REWARD = best_reward
            _LAST_PROMPT_FINGERPRINT = fp
            _HOF_CHANGE_COUNTER = 0
            if added > 0:
                print(f"[SUPEXP] heuristic-added {added} expressions to {SUPEXP_FILE}", flush=True)
                return added

    if not os.getenv("OPENAI_API_KEY", "").strip():
        return 0

    try:
        openai_module = importlib.import_module("openai")
        client = openai_module.OpenAI()

        t0 = time.time()
        response = client.responses.create(
            model=SUPEXP_MODEL,
            input=_build_prompt(hall_of_fame, nvars),
            max_output_tokens=SUPEXP_MAX_OUTPUT_TOKENS,
            timeout=SUPEXP_TIMEOUT_SECONDS,
        )
        raw = getattr(response, "output_text", "")
        print(f"[SUPEXP] LLM call completed in {time.time() - t0:.2f}s", flush=True)
        _CALL_COUNT += 1
        _FAIL_STREAK = 0
        _HOF_CHANGE_COUNTER = 0
    except Exception as e:
        _LAST_PUSH_TS = time.time()
        _CALL_COUNT += 1
        _FAIL_STREAK += 1
        _HOF_CHANGE_COUNTER = 0
        print(f"[SUPEXP] generation request failed: {e}", flush=True)
        return 0

    candidates = _parse_json_or_lines(raw)
    for c in candidates:
        s = _sanitize_subexpression(c, nvars)
        if not s or s in seen:
            continue
        cleaned.append(s)
        seen.add(s)
        if len(cleaned) >= SUPEXP_MAX_SUGGESTIONS:
            break

    if not cleaned:
        for a in _heuristic_atoms_from_hof(hall_of_fame, nvars):
            s = _sanitize_subexpression(a, nvars)
            if not s or s in seen:
                continue
            cleaned.append(s)
            seen.add(s)
            if len(cleaned) >= SUPEXP_MAX_SUGGESTIONS:
                break

    if not SUPEXP_AUTO_APPEND:
        if cleaned:
            print(f"[SUPEXP] generated {len(cleaned)} suggestions (auto-append disabled)", flush=True)
        _LAST_PUSH_TS = time.time()
        _LAST_PUSH_BEST_REWARD = best_reward
        _LAST_PROMPT_FINGERPRINT = fp
        return 0

    added = _append_unique_lines(SUPEXP_FILE, cleaned)
    _LAST_PUSH_TS = time.time()
    _LAST_PUSH_BEST_REWARD = best_reward
    _LAST_PROMPT_FINGERPRINT = fp
    if added > 0:
        print(f"[SUPEXP] added {added} expressions to {SUPEXP_FILE}", flush=True)
    else:
        print(f"[SUPEXP] no new expressions added; file: {SUPEXP_FILE}", flush=True)
    return added