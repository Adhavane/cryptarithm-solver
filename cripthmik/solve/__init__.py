"""This module contains the classes that are used to solve the puzzles.

Classes:
    Solver: Abstract class for a solver that solves cryptarithms.
    PrologSolver: A solver that uses Prolog to solve cryptarithms.
    Enumerate: A solver that uses Enumeration to solve cryptarithms.
    GenerateAndTest: A solver that uses Generate and Test to solve cryptarithms.

Example:
    >>> from cripthmik.solve import Solver
    >>> class MySolver(Solver):
    ...     def solve(self, cryptarithm: Cryptarithm) -> Generator[Solution, None, None]:
    ...         pass
"""


from ._enumerate import Enumerate
from ._generate_and_test import GenerateAndTest
from ._prolog import PrologSolver
from ._solver import Solver

__all__ = ["Solver", "PrologSolver", "GenerateAndTest", "Enumerate"]
