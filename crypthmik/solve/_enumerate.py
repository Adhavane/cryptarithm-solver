import itertools
import re
from typing import Generator, Set

from tqdm import tqdm

from ..utils import Cryptarithm, Letter, Solution
from ._solver import Solution, Solver


class Enumerate(Solver):
    """A solver that uses Enumeration to solve cryptarithms.

    Attributes:
        None

    Methods:
        _generate_perms: Generates all possible permutations of the variables.
        _evaluated_expr: Evaluates an expression and returns True if it is valid.
        _valid_solution: Checks if a solution is valid.
        solve: Solves a cryptarithm using Enumeration.

    Example:
        >>> from cripthmik.solve import Enumerate
        >>> solver = Enumerate()
        >>> cryptarithm = Cryptarithm("SEND + MORE = MONEY")
        >>> for solution in solver.solve(cryptarithm):
        ...     print(solution)
    """

    def __init__(self):
        super().__init__()

    def _generate_perms(self, letters: Set[Letter]) -> Generator[Solution, None, None]:
        for perm in itertools.permutations(range(10), len(letters)):
            sol = dict(zip(letters, perm))
            yield sol

    def _evaluated_expr(self, expression: str) -> bool:
        try:
            return bool(eval(expression))
        except ZeroDivisionError:
            return False
        except SyntaxError:
            return False
        except:  # Unknown error
            return False

    def _valid_solution(
        self, inst_expression: str, allow_zero: bool, allow_leading_zero: bool
    ) -> bool:
        # If the expression contains a leading zero, return False
        if (
            not allow_leading_zero
            and re.search(r"\b0+([1-9]*)", inst_expression) is not None
        ):
            return False
        # If the expression contains a non-leading zero, return False
        if (
            not allow_zero
            and allow_leading_zero
            and re.search(r"\b([1-9]+)0+([1-9]*)", inst_expression) is not None
        ):
            return False

        # Trim leading zeros
        inst_expression = inst_expression.replace("=", "==")
        inst_expression = re.sub(r"\b0+(\d+)", r"\1", inst_expression)

        # Evaluate the instantiated expression
        return self._evaluated_expr(inst_expression)

    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        # Generate all possible permutations of the variables
        permutations_gen = self._generate_perms(cryptarithm.letters)

        # Iterate over all permutations
        for perm in tqdm(permutations_gen, disable=True):
            # Instantiate the expression with the current permutation
            inst_expression = cryptarithm.instantiate(perm)

            # If the solution is valid, yield it
            if self._valid_solution(inst_expression, allow_zero, allow_leading_zero):
                yield perm
