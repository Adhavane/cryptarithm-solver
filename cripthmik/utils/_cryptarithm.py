import re

OPERATORS = ['+', '-', '*', '/', '%', '=']


class Cryptarithm:
    """Cryptarithm class for solving cryptarithm puzzles."""

    def __init__(self, puzzle: str, case_sensitive: bool = False):
        puzzle = Cryptarithm.format_puzzle(puzzle, case_sensitive)
        Cryptarithm.validate_puzzle(puzzle)

        self._puzzle: str = puzzle

    @staticmethod
    def format_puzzle(puzzle: str, case_sensitive: bool):
        if not case_sensitive:  # Convert to uppercase if not case sensitive
            puzzle = puzzle.upper()
        puzzle = puzzle.replace(' ', '')  # Remove spaces
        return puzzle

    @staticmethod
    def validate_puzzle(puzzle: str):
        # Check if puzzle is a string
        if not isinstance(puzzle, str):
            raise ValueError('Puzzle must be a string.')

        # Check if puzzle is in the form 'WORD [OPERATOR] WORD ([OPERATOR] WORD)* = WORD ([OPERATOR] WORD)*'
        pattern = r'^[a-zA-Z]+(?:[+*/%-][a-zA-Z]+)*=[a-zA-Z]+(?:[+*/%-][a-zA-Z]+)*$'
        if not re.match(pattern, puzzle):
            raise ValueError('Invalid puzzle format.')

    def get_puzzle(self):
        return self._puzzle


if __name__ == '__main__':
    puzzle = 'SEnD +MORE = MONEY'
    cryptarithm = Cryptarithm(puzzle)
    print(cryptarithm.get_puzzle())
