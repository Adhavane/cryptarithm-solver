from typing import List, Set

from ..utils import PrologCryptarithm, PrologRule
from ._prolog import PrologSolver


class GenerateAndTest(PrologSolver):
    """A solver that uses Generate and Test to solve cryptarithms.

    Attributes:
        rules: A list of rules that are used to solve the cryptarithm.

    Methods:
        _all_digits: Generates rules for all the digits in the cryptarithm.
        _all_diff: Generates a rule that ensures all the digits are different.
        _diff: Generates a rule that ensures a digit is different from a value.
        _generate: Generates rules for the cryptarithm.
        _test: Generates a rule that tests the cryptarithm.
        _query_rules: Generates the rules that are used to solve the cryptarithm.

    Example:
        >>> from cripthmik.solve import GenerateAndTest
        >>> solver = GenerateAndTest()
        >>> cryptarithm = Cryptarithm("SEND + MORE = MONEY")
        >>> for solution in solver.solve(cryptarithm):
        ...     print(solution)
    """

    _rules: List[PrologRule] = [
        "digit(X) :- member(X, [0,1,2,3,4,5,6,7,8,9])",
        "all_diff([])",
        "all_diff([H|T]) :- \+member(H, T), all_diff(T)",
    ]

    def __init__(self):
        super().__init__()

    def _all_digits(self, letters: Set[str]) -> Set[PrologRule]:
        return {f"digit({letter})" for letter in letters}

    def _all_diff(self, letters: Set[str]) -> PrologRule:
        return f"all_diff([{','.join(letters)}])"

    def _diff(self, letter: str, value: int) -> PrologRule:
        return f"dif({letter}, {value})"

    def _generate(
        self, pl_cryptarithm: PrologCryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> List[PrologRule]:
        generated = []

        generated += list(self._all_digits(pl_cryptarithm.letters))
        generated.append(self._all_diff(pl_cryptarithm.letters))
        if not allow_zero:
            for char in pl_cryptarithm.letters:
                generated.append(self._diff(char, 0))
        if not allow_leading_zero:
            for char in pl_cryptarithm.leading_letters:
                generated.append(self._diff(char, 0))
        if allow_leading_zero:
            for char in pl_cryptarithm.leading_letters:
                if f"dif({char}, 0)" in generated:
                    generated.remove(self._diff(char, 0))

        return generated

    def _test(self, pl_cryptarithm: PrologCryptarithm) -> PrologRule:
        operands = pl_cryptarithm.words
        operators = pl_cryptarithm.operators
        rule = ""

        for i in range(len(operators)):
            rule += "("
            for char, coef in zip(operands[i], range(len(operands[i]), 0, -1)):
                rule += f"{10 ** (coef - 1)} * {char} + "
            rule = rule[:-3] + ")"
            rule += f" {operators[i]} "
        rule += "("
        for char, coef in zip(operands[-1], range(len(operands[-1]), 0, -1)):
            rule += f"{10 ** (coef - 1)} * {char} + "
        rule = rule[:-3] + ")"
        rule = rule.replace("=", "=:=")  # Replace = with =:= for Prolog

        return rule

    def _query_rules(
        self, pl_cryptarithm: PrologCryptarithm,
        allow_zero: bool, allow_leading_zero: bool
    ) -> List[PrologRule]:
        return self._generate(pl_cryptarithm, allow_zero, allow_leading_zero) + [
            self._test(pl_cryptarithm)
        ]
