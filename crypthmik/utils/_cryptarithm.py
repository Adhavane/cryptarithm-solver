import re
from typing import Dict, List, Set

from ._types import Solution


class Cryptarithm:
    """Cryptarithm class for solving cryptarithm puzzles.

    Parameters:
        puzzle (str): The cryptarithm puzzle to solve.
        case_sensitive (bool): Whether the puzzle is case sensitive. Default is False.

    Attributes:
        _operators_map (Dict[str, str]): Mapping of operators to symbols.
        puzzle (str): The formatted puzzle.
        case_sensitive (bool): Whether the puzzle is case sensitive.
        words (List[str]): List of words in the puzzle.
        letters (Set[str]): Set of unique letters in the puzzle.
        leading_letters (Set[str]): Set of leading letters in the puzzle.
        operators (List[str]): List of operators in the puzzle.

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

    _operators_map: Dict[str, str] = {
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
        self._case_sensitive: bool = case_sensitive

    def _format_puzzle(self, puzzle: str, case_sensitive: bool = False) -> str:
        if not case_sensitive:  # Convert to uppercase if not case sensitive
            puzzle = puzzle.upper()
        puzzle = puzzle.replace(" ", "")  # Remove spaces
        return puzzle

    def _validate_puzzle(self, puzzle: str) -> None:
        # Check if puzzle is a string
        if not isinstance(puzzle, str):
            raise ValueError("Puzzle must be a string.")

        # Check if puzzle is not empty
        if puzzle.count(self._operators_map["equals"]) != 1:
            raise ValueError("Puzzle must contain exactly one equals sign.")

        # Check if puzzle contains only valid characters
        pattern = (
            r"^[a-zA-Z]+(?:["
            + "".join([f"\\{op}" for op in self._operators_map.values()])
            + r"][a-zA-Z]+)+$"
        )
        if not re.match(pattern, puzzle):
            raise ValueError("Invalid puzzle format.")

    @property
    def puzzle(self) -> str:
        return self._puzzle

    @property
    def case_sensitive(self) -> bool:
        return self._case_sensitive

    @property
    def words(self) -> List[str] | List[List[str]]:
        return re.findall(r"[a-zA-Z]+", self._puzzle)

    @property
    def letters(self) -> Set[str]:
        return set("".join(self.words))

    @property
    def leading_letters(self) -> Set[str]:
        return set([word[0] for word in self.words])

    @property
    def operators(self) -> List[str]:
        pattern = "[" + \
            "".join([f"\\{op}" for op in self._operators_map.values()]) + "]"
        return re.findall(pattern, self._puzzle)

    def instantiate(self, solution: Solution) -> str:
        return "".join(map(lambda c: str(solution.get(c, c)), self._puzzle))
