import re
from typing import Set


class Cryptarithm:
    """Cryptarithm class for solving cryptarithm puzzles.

    Parameters:
        puzzle (str): The cryptarithm puzzle to solve.
        case_sensitive (bool): Whether the puzzle is case sensitive. Default is False.

    Attributes:
        puzzle (str): The formatted puzzle.
        words (Set[str]): Set of words in the puzzle.
        letters (Set[str]): Set of unique letters in the puzzle.
        operators (Set[str]): Set of operators in the puzzle.

    Methods:
        _format_puzzle: Format the puzzle.
        _validate_puzzle: Validate the puzzle.

    Raises:
        ValueError: If the puzzle is not a string, does not contain exactly one equals sign, or is in an invalid format.

    Example:
        >>> puzzle = Cryptarithm("SEND + MORE = MONEY")
        >>> puzzle.puzzle
        'SEND+MORE=MONEY'
        >>> puzzle.words
        {'SEND', 'MORE', 'MONEY'}
        >>> puzzle.letters
        {'S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'}
        >>> puzzle.operators
        {'+', '='}
    """

    _operators = {
        "addition": "+",
        "subtraction": "-",
        "multiplication": "*",
        "division": "/",
        "modulus": "%",
        "equals": "=",
    }

    def __init__(self, puzzle: str, case_sensitive: bool = False):
        puzzle = self._format_puzzle(puzzle, case_sensitive)
        self._validate_puzzle(puzzle)

        self._puzzle: str = puzzle

    @classmethod
    def _format_puzzle(cls, puzzle: str, case_sensitive: bool = False) -> str:
        if not case_sensitive:  # Convert to uppercase if not case sensitive
            puzzle = puzzle.upper()
        puzzle = puzzle.replace(" ", "")  # Remove spaces
        return puzzle

    @classmethod
    def _validate_puzzle(cls, puzzle: str) -> None:
        # Check if puzzle is a string
        if not isinstance(puzzle, str):
            raise ValueError("Puzzle must be a string.")

        # Check if puzzle is not empty
        if puzzle.count(cls._operators["equals"]) != 1:
            raise ValueError("Puzzle must contain exactly one equals sign.")

        # Check if puzzle contains only valid characters
        pattern = (
            r"^[a-zA-Z]+(?:["
            + "".join([f"\\{op}" for op in cls._operators.values()])
            + r"][a-zA-Z]+)+$"
        )
        if not re.match(pattern, puzzle):
            raise ValueError("Invalid puzzle format.")

    @property
    def puzzle(self) -> str:
        return self._puzzle

    @property
    def words(self) -> Set[str]:
        return set(re.findall(r"[a-zA-Z]+", self._puzzle))

    @property
    def letters(self) -> Set[str]:
        return set("".join(self.words))

    @property
    def operators(self) -> Set[str]:
        pattern = "[" + \
            "".join([f"\\{op}" for op in self._operators.values()]) + "]"
        return set(re.findall(pattern, self._puzzle))
