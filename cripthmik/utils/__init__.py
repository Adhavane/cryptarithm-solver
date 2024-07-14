"""This module contains the Cryptarithm class.

A cryptarithm is a type of mathematical puzzle in which the digits are replaced by letters of the alphabet or other symbols. The goal is to find the correct mapping between the letters and the digits to satisfy the given equation.

Example:
    The cryptarithm "SEND + MORE = MONEY" can be solved as follows:
    S = 9, E = 5, N = 6, D = 7, M = 1, O = 0, R = 8, Y = 2
    Therefore, the solution is "9567 + 1085 = 10652".
    
Attributes:
    OPERATORS (List[str]): List of valid operators for the cryptarithm puzzle.
    
Classes:
    Cryptarithm: Class for solving cryptarithm puzzles.
"""


from ._cryptarithm import Cryptarithm

__all__ = ["Cryptarithm"]
