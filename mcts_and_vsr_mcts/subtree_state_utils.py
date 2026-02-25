from typing import List, Tuple


def production_rules_to_seq(list_of_production_rules: List[str]) -> List[str]:
    """
    Same logic as production_rules_to_expr, but returns the expanded token list (seq)
    so we can reliably detect remaining nonterminals like 'A'.
    """
    seq = ["f"]
    for one_rule in list_of_production_rules:
        lhs = one_rule[0]        # e.g. 'A' from "A->(A-A)"
        rhs = list(one_rule[3:]) # list of characters after '->'
        for ix, s in enumerate(seq):
            if s == lhs:
                seq = seq[:ix] + rhs + seq[ix + 1:]
                break
    return seq


def state_to_subexpr_string(state: str, max_rules: int = 25, nonterminal: str = "A") -> Tuple[str, bool, List[str]]:
    """
    Converts a production-rule state string "f->A,A->...,A->..." into:
      (expr_str, is_complete, seq_tokens)

    is_complete is True iff the expanded token stream no longer contains `nonterminal`.
    """
    rules = state.split(",")
    if max_rules and len(rules) > max_rules:
        rules = rules[:max_rules]

    seq = production_rules_to_seq(rules)
    is_complete = (nonterminal not in seq)

    expr_str = "".join(seq)
    return expr_str, is_complete, seq