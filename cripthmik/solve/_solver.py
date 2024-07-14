from abc import ABC, abstractmethod
from typing import Dict, Generator, TypeAlias

from ..utils import Cryptarithm

Solution: TypeAlias = Dict[str, int]


class Solver(ABC):
    """Abstract class for a solver that solves cryptarithms.

    Methods:
        solve: Abstract method that solves a cryptarithm.

    Raises:
        NotImplementedError: If the solve method is not implemented.

    Example:
        >>> from cripthmik.solve import Solver
        >>> class MySolver(Solver):
        ...     def solve(
        ...         self, cryptarithm: Cryptarithm,
        ...         allow_zero: bool = True, allow_leading_zero: bool = False
        ...     ) -> Generator[Solution, None, None]:
        ...         pass
    """

    @abstractmethod
    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        pass
