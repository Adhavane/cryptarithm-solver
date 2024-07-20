from typing import Generator, Set

from ..utils import Cryptarithm
from ._solver import Solution, Solver
import itertools
from tqdm import tqdm


class Enumerate(Solver):
    
    def __init__(self):
        super().__init__()

    def _generate_perms(self, letters: str, leading_letters: Set[str]) -> Generator[Solution, None, None]:
        for perm in itertools.permutations(range(10), len(letters)):
            sol = dict(zip(letters, perm))
            yield sol
            
    def instantiateExpr(expr: str, perm: Solution) -> str:
        return "".join(map(lambda c: str(perm.get(c, c)), expr))
            
    def trimLeadingZero(inst_expr: str) -> str:
        return re.sub(r"\b0+(\d+)", r"\1", inst_expr)

    def evalExpr(expr: str) -> bool:
        try:
            return eval(expr)
        except ZeroDivisionError:
            print(f"Zero division error in expression: {expr}")
            return False
        except SyntaxError:
            print(f"Syntax error in expression: {expr}")
            return False
        except:
            print(f"Unknown error in expression: {expr}")
            return False
        
    def isLeadingZero(expr: str) -> bool:
        return re.search(r"\b0+(\d+)", expr) is not None

    def _valid_solution(
        self, cryptarithm: Cryptarithm,
        solution: Solution, allow_zero: bool, allow_leading_zero: bool
    ) -> bool:
        # Instantiate the expression with the current permutation
        inst_expr = self.instantiateExpr(expr_trimmed, perm)

        if not allow_leading_zero and isLeadingZero(inst_expr):
            continue

        inst_expr = trimLeadingZero(inst_expr)

        # Evaluate the instantiated expression
        if evalExpr(inst_expr):
            yield perm

    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        # Generate all possible permutations of the variables
        gen_perms = self._generate_perms(cryptarithm.letters, cryptarithm.leading_letters)

        for perm in tqdm(gen_perms):
            if _valid_solution(cryptarithm, perm, allow_zero, allow_leading_zero):
                # If the solution is valid, yield it
                yield perm
