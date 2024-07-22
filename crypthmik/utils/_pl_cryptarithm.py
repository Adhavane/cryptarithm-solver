import re
from typing import List, Set

from ._cryptarithm import Cryptarithm


class PrologCryptarithm(Cryptarithm):
    """Cryptarithm class for solving cryptarithm puzzles.
    """
    
    lowercase_suffix = "_lowercase"

    def __init__(self, puzzle: str, case_sensitive: bool = False):
        super().__init__(puzzle, case_sensitive)

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
    def letters(self) -> Set[str]:
        return set("".join(self.words))
    
    @property
    def letters_2(self) -> Set[str]:
        # the letters in lowercase are converted to uppercase with a suffix
        # because the Prolog solver does not support lowercase letters
        pass

    @property
    def leading_letters(self) -> Set[str]:
        return set([word[0] for word in self.words])
    
    @property
    def leading_letters_2(self) -> Set[str]:
        # the letters in lowercase are converted to uppercase with a suffix
        # because the Prolog solver does not support lowercase letters
        return set([word[0] for word in self.words_2])
