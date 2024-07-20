from typing import Generator, Set

from ..utils import Cryptarithm
from ._solver import Solution, Solver
import itertools


class Enumerate(Solver):
    
    def __init__(self):
        super().__init__()

    def _generate_perms(self, letters: str, leading_letters: Set[str]) -> Generator[Solution, None, None]:
        for perm in itertools.permutations(range(10), len(letters)):
            sol = dict(zip(letters, perm))
            yield sol
            
    # def _valid_solution(self, cryptarithm: Cryptarithm, solution: Solution, allow_zero: bool, allow_leading_zero: bool) -> bool:
    #     # Instantiate the expression with the current permutation
    #     inst_expr = instantiateExpr(expr_trimmed, perm)

    #     if not allow_leading_zero and isLeadingZero(inst_expr):
    #         continue

    #     inst_expr = trimLeadingZero(inst_expr)

    #     # Evaluate the instantiated expression
    #     if evalExpr(inst_expr):
    #         # If the expression evaluates to True, yield the solution
    #         yield perm

    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        # Generate all possible permutations of the variables
        gen_perms = self._generate_perms(cryptarithm.letters, cryptarithm.leading_letters)

        # for perm in tqdm(gen_perms):
        #     if _valid_solution(cryptarithm, perm, allow_zero, allow_leading_zero):
        #         yield perm
