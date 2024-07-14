from typing import Generator, List, Set, TypeAlias

from pyswip import Prolog

from ..utils import Cryptarithm
from ._solver import Solution, Solver

Clause: TypeAlias = str


class GenerateAndTest(Solver):
    def __init__(self):
        super().__init__()
        self._prolog = Prolog()

    def _all_digits(self, cryptarithm: Cryptarithm) -> Set[Clause]:
        return {f"digit({letter})" for letter in cryptarithm.letters}

    def _all_diff(self, cryptarithm: Cryptarithm) -> Clause:
        return f"all_diff([{', '.join(cryptarithm.letters)}])"

    def _diff(self, letter: str, value: int) -> Clause:
        return f"dif({letter}, {value})"

    def _generate(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> List[Clause]:
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

    def solve(self, cryptarithm: Cryptarithm) -> Generator[Solution, None, None]:
        pass
