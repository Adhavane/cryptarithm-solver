from typing import Generator

from ..utils import Cryptarithm
from ._solver import Solution, Solver
import itertools


class Enumerate(Solver):
    
    def __init__(self):
        super().__init__()

    def _generate_perms(
        self, letters: str,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        for perm in itertools.permutations(range(10), len(letters)):
            yield dict(zip(letters, perm))

    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        # print("Enumerate")
        # print(cryptarithm.words)
        # print(cryptarithm.operators)
        # print(cryptarithm.letters)

        # Generate all possible permutations of the variables
        # gen_perms = _generate_perms(vars, allow_zero, allow_leading_zero)

        # for perm in tqdm(gen_perms):
        #     # Instantiate the expression with the current permutation
        #     inst_expr = instantiateExpr(expr_trimmed, perm)

        #     if not allow_leading_zero and isLeadingZero(inst_expr):
        #         continue

        #     inst_expr = trimLeadingZero(inst_expr)

        #     # Evaluate the instantiated expression
        #     if evalExpr(inst_expr):
        #         # If the expression evaluates to True, yield the solution
        #         yield perm
