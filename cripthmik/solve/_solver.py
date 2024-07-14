from abc import ABC, abstractmethod
from typing import Dict, Generator, TypeAlias
from cripthmik.utils import Cryptarithm

Solution: TypeAlias = Dict[str, int]


class Solver(ABC):
    """Abstract class for a solver that solves cryptarithms.

    Methods:
        solve(cryptarithm: Cryptarithm) -> Generator[Solution, None, None]: Solves the cryptarithm puzzle.

    Raises:
        NotImplementedError: If the solve method is not implemented.

    Example:
        >>> from cripthmik.solve import Solver
        >>> class MySolver(Solver):
        ...     def solve(self, cryptarithm: Cryptarithm) -> Generator[Solution, None, None]:
        ...         pass
    """

    @abstractmethod
    def solve(self, cryptarithm: Cryptarithm) -> Generator[Solution, None, None]:
        pass
