import re
from typing import List, Set

from multipledispatch import dispatch

from ._cryptarithm import Cryptarithm


class PrologCryptarithm(Cryptarithm):
    """Cryptarithm class for solving cryptarithm puzzles.
    """

    lowercase_suffix = "_lowercase"

    @dispatch(str, bool)
    def __init__(self, puzzle: str, case_sensitive: bool = False):
        super().__init__(puzzle, case_sensitive)
    
    @dispatch(Cryptarithm)
    def __init__(self, cryptarithm: Cryptarithm):
        super().__init__(cryptarithm.puzzle, cryptarithm.case_sensitive)

    @property
    def words(self) -> List[str]:
        return re.findall(r"[a-zA-Z]+", self._puzzle)

    @property
    def words_2(self) -> List[List[str]]:
        # the letters in lowercase are converted to uppercase with a suffix
        # because the Prolog solver does not support lowercase letters
        words = []
        for word in self.words:
            word_2 = []
            for letter in word:
                if letter.islower():
                    word_2.append(letter.upper() + self.lowercase_suffix)
                else:
                    word_2.append(letter)
            words.append(word_2)
        return words
    
    @property
    def words_2_opt_with_map(self) -> List[List[str]]:
        return list(
            map(
                lambda word:
                    list(map(
                        lambda letter: letter.upper() + self.lowercase_suffix if letter.islower() else letter,
                        word
                    )
                ),
                self.words
            )
        )

    @property
    def letters(self) -> Set[str]:
        return set("".join(self.words))
    
    @property
    def letters_2(self) -> Set[str]:
        # the letters in lowercase are converted to uppercase with a suffix
        # because the Prolog solver does not support lowercase letters
        # the letters are flattened to a single set
        return set([letter for word in self.words_2 for letter in word])

    @property
    def leading_letters(self) -> Set[str]:
        return set([word[0] for word in self.words])
    
    @property
    def leading_letters_2(self) -> Set[str]:
        # the letters in lowercase are converted to uppercase with a suffix
        # because the Prolog solver does not support lowercase letters
        return set([word[0] for word in self.words_2])
