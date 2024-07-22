from typing import List, Set

from multipledispatch import dispatch

from ._cryptarithm import Cryptarithm


class PrologCryptarithm(Cryptarithm):
    """Class for solving cryptarithm puzzles using Prolog.

    This class extends the Cryptarithm class by providing additional methods for
    converting the puzzle to a format that can be solved using Prolog.

    Parameters:
        puzzle (str): The cryptarithm puzzle to solve.
        case_sensitive (bool): Whether the puzzle is case sensitive. Default is True.

        cryptarithm (Cryptarithm): A Cryptarithm object.

    Attributes:
        words (List[List[str]]): List of words in the puzzle in Prolog format.
        letters (Set[str]): Set of letters in the puzzle.
        leading_letters (Set[str]): Set of leading letters in the puzzle.

    Example:
        >>> puzzle = PrologCryptarithm("My + Name = Is", case_sensitive=True)
        >>> puzzle.words
        [['M', 'Y_lowercase'], ['N', 'A', 'M', 'E_lowercase'], ['I', 'S_lowercase']]
        >>> puzzle.letters
        {'Y_lowercase', 'M', 'E_lowercase', 'N', 'A', 'I', 'S_lowercase'}
        >>> puzzle.leading_letters
        {'M', 'N', 'I'}
    """

    _lowercase_suffix = "_lowercase"

    @dispatch(str, bool)
    def __init__(self, puzzle: str, case_sensitive: bool = True):
        super().__init__(puzzle, case_sensitive)

    @dispatch(Cryptarithm)
    def __init__(self, cryptarithm: Cryptarithm):
        super().__init__(cryptarithm.puzzle, cryptarithm.case_sensitive)

    @property
    def words(self) -> List[str] | List[List[str]]:
        # Convert the words to Prolog format by adding the lowercase suffix to
        # the lowercase letters.
        # This is necessary because Prolog is case-sensitive, so we need to
        # distinguish between uppercase and lowercase letters.
        return list(
            map(
                lambda word: list(
                    map(
                        lambda letter: (
                            letter.upper() + self._lowercase_suffix
                            if letter.islower()
                            else letter
                        ),
                        word,
                    )
                ),
                super().words,
            )
        )

    @property
    def letters(self) -> Set[str]:
        return set([letter for word in self.words for letter in word])

    @property
    def leading_letters(self) -> Set[str]:
        return set([word[0] for word in self.words])
