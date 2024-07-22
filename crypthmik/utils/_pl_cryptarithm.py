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
        words_prolog (List[List[str]]): List of words in the puzzle in Prolog format.
        variables (Set[str]): Set of unique variables in the puzzle.
        leading_variables (Set[str]): Set of leading variables in the puzzle.

    Example:
        >>> puzzle = PrologCryptarithm("My + Name = Is", case_sensitive=True)
        >>> puzzle.words_prolog
        [['M', 'Y_lowercase'], ['N', 'A', 'M', 'E_lowercase'], ['I', 'S_lowercase']]
        >>> puzzle.variables
        {'Y_lowercase', 'M', 'E_lowercase', 'N', 'A', 'I', 'S_lowercase'}
        >>> puzzle.leading_variables
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
    def words_prolog(self) -> List[List[str]]:
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
                self.words,
            )
        )

    @property
    def variables(self) -> Set[str]:
        return set([letter for word in self.words_prolog for letter in word])

    @property
    def leading_variables(self) -> Set[str]:
        return set([word[0] for word in self.words_prolog])
