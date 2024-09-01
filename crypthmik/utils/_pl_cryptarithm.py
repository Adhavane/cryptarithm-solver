from typing import List, Set

from multipledispatch import dispatch

from ._cryptarithm import Cryptarithm
from ._types import Letter, PrologLetter, PrologSolution, Solution, Word


class PrologCryptarithm(Cryptarithm):
    """Class for solving cryptarithm puzzles using Prolog.

    This class extends the Cryptarithm class by providing additional methods for
    converting the puzzle to a format that can be solved using Prolog.

    Parameters:
        puzzle (str): The cryptarithm puzzle to solve.
        case_sensitive (bool): Whether the puzzle is case sensitive. Default is True.

        cryptarithm (Cryptarithm): A Cryptarithm object.

    Attributes:
        words (List[Word]): List of words in the puzzle in Prolog format.
        letters (Set[Letter]): Set of letters in the puzzle.

    Methods:
        _convert_to_prolog_letter: Convert a letter to Prolog format.
        _convert_from_prolog_letter: Convert a Prolog letter to standard format.
        convert_solution: Convert a Prolog solution to a standard solution.

    Example:
        >>> puzzle = PrologCryptarithm("My + Name = Is", case_sensitive=True)
        >>> puzzle.words
        [['M', 'Y_lowercase'], ['N', 'A', 'M', 'E_lowercase'], ['I', 'S_lowercase']]
        >>> puzzle.letters
        {'Y_lowercase', 'M', 'E_lowercase', 'N', 'A', 'I', 'S_lowercase'}
    """

    _lowercase_suffix = "_lowercase"

    @dispatch(str, bool)
    def __init__(self, puzzle: str, case_sensitive: bool = True):
        super().__init__(puzzle, case_sensitive)

    @dispatch(Cryptarithm)
    def __init__(self, cryptarithm: Cryptarithm):
        super().__init__(cryptarithm.puzzle, cryptarithm.case_sensitive)

    @property
    def words(self) -> List[Word]:
        # Convert the words to Prolog format by adding the lowercase suffix to
        # the lowercase letters.
        # This is necessary because Prolog is case-sensitive, so we need to
        # distinguish between uppercase and lowercase letters.
        return list(
            map(
                lambda word: list(
                    map(lambda letter: self._convert_to_prolog_letter(letter), word)
                ),
                super().words,
            )
        )

    def _convert_to_prolog_letter(self, letter: Letter) -> PrologLetter:
        return letter.upper() + self._lowercase_suffix if letter.islower() else letter

    def _convert_from_prolog_letter(self, pl_letter: PrologLetter) -> Letter:
        return (
            pl_letter[:-len(self._lowercase_suffix)].lower()
            if pl_letter.endswith(self._lowercase_suffix)
            else pl_letter
        )

    @property
    def letters(self) -> Set[str]:
        return set([letter for word in self.words for letter in word])

    def convert_solution(self, pl_solution: PrologSolution) -> Solution:
        return {
            self._convert_from_prolog_letter(key): value
            for key, value in pl_solution.items()
        }
