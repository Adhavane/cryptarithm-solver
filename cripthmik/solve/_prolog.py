from _solver import Solver
from pyswip import Prolog
from ..utils import Cryptarithm

from typing import List, TypeAlias, Set

Clause: TypeAlias = str
class PrologSolver(Solver):
    def __init__(self):
        super().__init__()
        self._prolog = Prolog()
        

    def _all_digits(self, cryptarithm: Cryptarithm) -> Set[Clause]:
        return {f"digit({letter})" for letter in cryptarithm.letters}
    
    def solve(self):
        pass


if __name__ == "__main__":
    prolog_solver = PrologSolver()
    print(prolog_solver._all_digits(Cryptarithm("SEND+MORE=MONEY")))
