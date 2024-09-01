"""Type aliases for the cripthmik package."""


from typing import Dict, List, TypeAlias

Letter: TypeAlias = str
Word: TypeAlias = List[Letter]
Solution: TypeAlias = Dict[str, int]

PrologLetter: TypeAlias = str
PrologSolution: TypeAlias = Dict[str, int]
PrologRule: TypeAlias = str
