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
    Letter: Type alias for a letter in a cryptarithm.
    Word: Type alias for a word in a cryptarithm.
    Solution: Type alias for a dictionary containing the solution to a cryptarithm.
    PrologLetter: Type alias for a Prolog letter in a cryptarithm.
    PrologRule: Type alias for a Prolog rule in a cryptarithm.
    PrologSolution: Type alias for a Prolog solution in a cryptarithm.

Classes:
    Cryptarithm: Class for solving cryptarithm puzzles.
    PrologCryptarithm: Class for solving cryptarithm puzzles using Prolog.
"""


from ._cryptarithm import Cryptarithm
from ._pl_cryptarithm import PrologCryptarithm
from ._types import (Letter, PrologLetter, PrologRule, PrologSolution,
                     Solution, Word)

__all__ = [
    "Cryptarithm",
    "PrologCryptarithm",
    "Letter",
    "Word",
    "Solution",
    "PrologLetter",
    "PrologSolution",
    "PrologRule",
]
