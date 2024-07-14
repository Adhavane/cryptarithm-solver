from typing import Generator, List, Set, TypeAlias

from pyswip import Prolog

from ..utils import Cryptarithm
from ._solver import Solution, Solver

Rule: TypeAlias = str


class GenerateAndTest(Solver):
    def __init__(self):
        super().__init__()
        self._prolog = Prolog()

    def _all_digits(self, cryptarithm: Cryptarithm) -> Set[Rule]:
        return {f"digit({letter})" for letter in cryptarithm.letters}

    def _all_diff(self, cryptarithm: Cryptarithm) -> Rule:
        return f"all_diff([{', '.join(cryptarithm.letters)}])"

    def _diff(self, letter: str, value: int) -> Rule:
        return f"dif({letter}, {value})"

    def _generate(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> List[Rule]:
        generated = []

        generated += list(self._all_digits(cryptarithm))
        generated.append(self._all_diff(cryptarithm))
        if not allow_zero:
            for char in cryptarithm.letters:
                generated.append(self._diff(char, 0))
        if not allow_leading_zero:
            for char in cryptarithm.leading_letters:
                generated.append(self._diff(char, 0))
        if allow_leading_zero:
            for char in cryptarithm.leading_letters:
                if f"dif({char}, 0)" in generated:
                    generated.remove(self._diff(char, 0))

        return generated

    def _test(self, cryptarithm: Cryptarithm) -> Rule:
        operands = cryptarithm.words
        operators = cryptarithm.operators
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

    def solve(self, cryptarithm: Cryptarithm) -> Generator[Solution, None, None]:
        pass
