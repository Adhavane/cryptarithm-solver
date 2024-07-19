from typing import Generator, List, Set, TypeAlias

from pyswip import Prolog

from ..utils import Cryptarithm
from ._solver import Solution, Solver

import tempfile
from pathlib import Path

Rule: TypeAlias = str


class GenerateAndTest(Solver):
    """A solver that uses Generate and Test to solve cryptarithms.

    Attributes:
        rules: A list of rules that are used to solve the cryptarithm.

    Methods:
        solve: Solves a cryptarithm using Prolog.
        _all_digits: Generates rules for all the digits in the cryptarithm.
        _all_diff: Generates a rule that ensures all the digits are different.
        _diff: Generates a rule that ensures a digit is different from a value.
        _generate: Generates rules for the cryptarithm.
        _test: Generates a rule that tests the cryptarithm.

    Example:
        >>> from cripthmik.solve import GenerateAndTest
        >>> solver = GenerateAndTest()
        >>> cryptarithm = Cryptarithm("SEND + MORE = MONEY")
        >>> for solution in solver.solve(cryptarithm):
        ...     print(solution)
    """

    _rules: List[Rule] = [
        "digit(X) :- member(X, [0,1,2,3,4,5,6,7,8,9])",
        "all_diff([])",
        "all_diff([H|T]) :- \+member(H, T), all_diff(T)"
    ]

    def __init__(self):
        super().__init__()

    def _all_digits(self, cryptarithm: Cryptarithm) -> Set[Rule]:
        return {f"digit({letter})" for letter in cryptarithm.letters}

    def _all_diff(self, cryptarithm: Cryptarithm) -> Rule:
        return f"all_diff([{','.join(cryptarithm.letters)}])"

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

    def _query(self, cryptarithm: Cryptarithm) -> Rule:
        operators = cryptarithm.operators
        operands = cryptarithm.words
        query = ""

        for i in range(len(operands) - 1):
            query += f"[{','.join(operands[i])}], {operators[i]}, "
        query += f"[{','.join(operands[-1])}]"

        return f"solve([{query}])"

    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        # Generate rules and solve cryptarithm
        prolog = Prolog()  # Create a Prolog engine

        # Create a temporary file to store the rules
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
            for rule in self._rules:
                fp.write(rule + ".\n")
            fp.write("\n")

            query = self._query(cryptarithm)
            fp.write(f"{query} :- ")
            fp.write(", ".join(map(str, self._generate(
                cryptarithm, allow_zero, allow_leading_zero))))
            fp.write(f", {self._test(cryptarithm)}" + ".\n")

            fp.close()

            # Consult the temporary file and query the Prolog engine
            prolog.consult(Path(fp.name).as_posix())  # Convert to Posix path
            for solution in prolog.query(query):
                yield solution
