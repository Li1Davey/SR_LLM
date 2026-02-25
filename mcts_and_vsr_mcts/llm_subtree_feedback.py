# llm_subtree_feedback.py
import os
import json
import time
import hashlib
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

# --- knobs ---
LLM_BONUS_SCALE = float(os.getenv("SCIBENCH_LLM_BONUS_SCALE", "0.1"))

CACHE_PATH = os.getenv(
    "SCIBENCH_LLM_CACHE_PATH",
    os.path.expanduser("~/.cache/scibench_llm_subtree_cache.json")
)
CACHE_FLUSH_EVERY = int(os.getenv("SCIBENCH_LLM_CACHE_FLUSH_EVERY", "50"))

# How many subtrees to consider from a state (keep cost bounded)
MAX_SUBTREES = int(os.getenv("SCIBENCH_LLM_MAX_SUBTREES", "32"))

# If you want to disable calling any LLM, set 0 (still uses heuristic + caching)
ENABLE_LLM = os.getenv("SCIBENCH_LLM_ENABLE", "0") == "1"


@dataclass
class LLMSubtreeResult:
    bonus: float
    reason: str
    used_subtrees: int
    cache_hits: int


# -----------------------
# Cache utilities
# -----------------------
_cache: Dict[str, dict] = {}
_dirty_writes = 0


def _load_cache() -> None:
    global _cache
    try:
        if os.path.exists(CACHE_PATH):
            with open(CACHE_PATH, "r") as f:
                _cache = json.load(f)
    except Exception:
        _cache = {}


def _flush_cache() -> None:
    global _dirty_writes
    if _dirty_writes <= 0:
        return
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    tmp = CACHE_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(_cache, f)
    os.replace(tmp, CACHE_PATH)
    _dirty_writes = 0


_load_cache()


# -----------------------
# Subtree extraction
# -----------------------
def _state_to_rules(state: str) -> List[str]:
    # state looks like: "f->A,A->(A-A),A->X0,..."
    # sometimes you pass just the module string already in that format
    parts = [p.strip() for p in state.split(",") if p.strip()]
    return parts


def _expand_rules_to_expr_str(rules: List[str]) -> str:
    """
    Very lightweight inline version of your production_rules_to_expr idea:
    replace the first matching LHS occurrence each rule.
    Works on strings like:
      f->A
      A->(A-A)
      A->X0
      A->X1
    """
    seq = ["f"]
    for r in rules:
        if len(r) < 4 or "->" not in r:
            continue
        lhs, rhs = r.split("->", 1)
        lhs = lhs.strip()
        rhs = rhs.strip()
        for ix, s in enumerate(seq):
            if s == lhs:
                seq = seq[:ix] + list(rhs) + seq[ix + 1 :]
                break
    return "".join(seq)


def _hash_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def _enumerate_subtrees_from_state(state: str) -> List[Tuple[str, str]]:
    """
    Return list of (subtree_id, subtree_text).
    Here subtree_text is "prefix states" (rule prefixes) converted to expr strings.
    This is cheap + correlates well with common-subtree reuse.

    subtree_id is a stable hash over a canonical representation.
    """
    rules = _state_to_rules(state)
    # build prefix expressions: f->A, f->A,A->..., ...
    subtrees: List[Tuple[str, str]] = []
    cur: List[str] = []
    for r in rules:
        cur.append(r)
        expr = _expand_rules_to_expr_str(cur)
        # canonical-ish: remove whitespace
        canon = expr.replace(" ", "")
        sid = _hash_str(canon)
        subtrees.append((sid, canon))

    # keep only the last MAX_SUBTREES (deepest / most specific) by default
    if len(subtrees) > MAX_SUBTREES:
        subtrees = subtrees[-MAX_SUBTREES:]
    return subtrees


# -----------------------
# Scoring (heuristic + optional LLM)
# -----------------------
def _heuristic_bonus(subtree_expr: str) -> float:
    """
    Cheap local proxy that tends to be useful:
    - reward "structured" things: exp(), (X1-X0), ratios with (.+C) patterns
    - penalize obvious bloat
    """
    s = subtree_expr

    bonus = 0.0
    if "exp(" in s:
        bonus += 0.15
    if "(X1-X0)" in s or "(X0-X1)" in s:
        bonus += 0.20
    if "+C" in s and "/" in s:
        bonus += 0.10
    # bloat penalty
    if len(s) > 120:
        bonus -= 0.10
    if s.count("exp(") >= 3:
        bonus -= 0.10
    return bonus


def _llm_bonus_stub(subtree_expr: str) -> float:
    """
    Replace this with a real OpenAI call once you have quota.
    For now: return 0.0 so behavior is deterministic + cheap.
    """
    return 0.0


def get_llm_subtree_bonus(state: str) -> Optional[LLMSubtreeResult]:
    """
    Input: full production-rule state string.
    Output: aggregated bonus over *subtrees*, cached by subtree hash.
    """
    global _dirty_writes

    if not state or "->" not in state:
        return None

    subtrees = _enumerate_subtrees_from_state(state)

    total_bonus = 0.0
    cache_hits = 0
    used = 0

    for sid, expr in subtrees:
        used += 1
        if sid in _cache:
            cache_hits += 1
            total_bonus += float(_cache[sid].get("bonus", 0.0))
            continue

        b = _heuristic_bonus(expr)

        if ENABLE_LLM:
            b += _llm_bonus_stub(expr)

        _cache[sid] = {
            "bonus": b,
            "expr": expr,
            "ts": int(time.time()),
        }
        _dirty_writes += 1
        total_bonus += b

        if _dirty_writes >= CACHE_FLUSH_EVERY:
            _flush_cache()

    # final flush opportunistically
    _flush_cache()

    return LLMSubtreeResult(
        bonus=float(total_bonus),
        reason=f"subtree_bonus over {used} subtrees ({cache_hits} cache hits)",
        used_subtrees=used,
        cache_hits=cache_hits,
    )