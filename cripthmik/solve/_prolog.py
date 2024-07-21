import multiprocessing as mp
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generator, List, TypeAlias

from pyswip import Prolog

from ..utils import Cryptarithm
from ._solver import Solution, Solver

Rule: TypeAlias = str


class PrologSolver(Solver, ABC):
    """A solver that uses Prolog to solve cryptarithms.
    
    Attributes:
        rules: A list of rules that are used to solve the cryptarithm.
        
    Methods:
        _query: Generates the query that is used to solve the cryptarithm.
        solve: Solves the cryptarithm and yields the solutions.
        _solve_worker: Worker function that solves the cryptarithm.
        _query_rules: Generates the rules that are used to solve the cryptarithm.
        
    Example:
        >>> from cripthmik.solve import PrologSolver
        >>> class MySolver(PrologSolver):
        ...     def _query_rules(self, cryptarithm, allow_zero, allow_leading_zero):
        ...         pass
        >>> solver = MySolver()
        >>> cryptarithm = Cryptarithm("SEND + MORE = MONEY")
        >>> for solution in solver.solve(cryptarithm):
        ...     print(solution)
    """

    _rules: List[Rule] = []

    def __init__(self):
        super().__init__()

    def _query(self, cryptarithm: Cryptarithm) -> Rule:
        operators = cryptarithm.operators
        operands = cryptarithm.words
        query = ""

        for i in range(len(operands) - 1):
            query += f"[{','.join(operands[i])}], {operators[i]}, "
        query += f"[{','.join(operands[-1])}]"

        return f"solve([{query}])"

    def solve(
        self, cryptarithm: Cryptarithm,
        allow_zero: bool = True, allow_leading_zero: bool = False
    ) -> Generator[Solution, None, None]:
        # Create a new process with a queue
        result_channel = mp.Queue()
        result_end = mp.Queue()
        error_channel = mp.Queue()
        error_end = mp.Queue()

        # Start the worker process
        worker = mp.Process(
            target=self._solve_worker,
            args=(
                result_channel, result_end,
                error_channel, error_end,
                cryptarithm, allow_zero, allow_leading_zero,
            ),
        )
        worker.start()

        # Yield the queue
        while True:
            if result_end.empty() and error_end.empty():
                if not result_channel.empty():
                    yield result_channel.get()
            else:
                break

        # Close the worker process
        worker.join()

        # Raise an exception if an error occurred
        if not error_end.empty():
            raise error_channel.get()

        # Close the queues
        result_channel.close()
        result_end.close()
        error_channel.close()
        error_end.close()

    def _solve_worker(
        self,
        result_channel: mp.Queue, result_end: mp.Queue,
        error_channel: mp.Queue, error_end: mp.Queue,
        cryptarithm: Cryptarithm, allow_zero: bool = True,
        allow_leading_zero: bool = False,
    ) -> None:
        try:
            # Generate rules and solve cryptarithm
            prolog = Prolog()  # Create a Prolog engine

            # Create a temporary file to store the rules
            with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
                for rule in self._rules:
                    fp.write(rule + ".\n")
                fp.write("\n")

                query = self._query(cryptarithm)
                fp.write(f"{query} :- ")
                fp.write(", ".join(map(str, self._query_rules(
                    cryptarithm, allow_zero, allow_leading_zero))) + ".\n")
                fp.write("\n")

                fp.close()

                # Consult the temporary file and query the Prolog engine
                prolog.consult(Path(fp.name).as_posix())  # Convert to Posix path
                for solution in prolog.query(query):
                    result_channel.put(solution)
                result_end.put(None)
        except Exception as e:
            error_channel.put(e)
            error_end.put(None)

        return

    @abstractmethod
    def _query_rules(
        self, cryptarithm: Cryptarithm, allow_zero: bool, allow_leading_zero: bool
    ) -> List[Rule]:
        pass
