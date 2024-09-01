"""This module contains the Cryptarithm class.

A cryptarithm is a type of mathematical puzzle in which the digits are replaced
by letters of the alphabet or other symbols.

The goal is to find the correct mapping between the letters and the digits to
satisfy the given equation.

Example:
    The cryptarithm "SEND + MORE = MONEY" can be solved as follows:
    S = 9, E = 5, N = 6, D = 7, M = 1, O = 0, R = 8, Y = 2
    Therefore, the solution is "9567 + 1085 = 10652".

Types:
    Solution: Type alias for a dictionary containing the solution to a cryptarithm.

Classes:
    Cryptarithm: Class for solving cryptarithm puzzles.
    PrologCryptarithm: Class for solving cryptarithm puzzles using Prolog.
"""


from ._cryptarithm import Cryptarithm
from ._pl_cryptarithm import PrologCryptarithm
from ._types import PrologRule, PrologSolution, Solution

__all__ = [
    "Cryptarithm",
    "PrologCryptarithm",
    "Solution",
    "PrologSolution",
    "PrologRule",
]
