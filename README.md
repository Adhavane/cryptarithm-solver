# .ʞᴉɯɥʇdʎɹɔ 🧩🧠

## 📜 Table of Contents

- [📜 Table of Contents](#-table-of-contents)
- [🔍 Overview](#-overview)
- [📦 Dependencies](#-dependencies)
- [🗂️ Repository Structure](#️-repository-structure)
- [📥 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📚 Documentation](#-documentation)
  - [🔠 Cryptarithm class](#-cryptarithm-class)
  - [💡 Solution methods](#-solution-methods)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📫 Contact](#-contact)

## 🔍 Overview

ɔᴉɯɥʇdʎɹʞ is a simple and easy-to-use Python library designed for effortlessly **solving cryptarithms** with just a few lines of code.

Cryptarithms, also known as [alphametics](https://en.wikipedia.org/wiki/Verbal_arithmetic), are **puzzles** where digits are replaced by letters of the alphabet. The goal is to find the correct mapping of letters to digits to make a valid arithmetic equation. For example, in the cryptarithm `SEND + MORE = MONEY`, each letter represents a unique digit, and the task is to find the correct assignment of digits to letters **to make the equation true**.

The library provides several algorithms to tackle these puzzles, including brute-force, generate-and-test, and constraint programming methods. The *[brute-force method](https://en.wikipedia.org/wiki/Enumeration_algorithm)* involves exhaustively enumerating all possible combinations to find a solution. The *[generate-and-test](https://en.wikipedia.org/wiki/Trial_and_error)* approach iteratively generates potential solutions and tests their validity. Meanwhile, *[constraint programming](https://en.wikipedia.org/wiki/Constraint_programming)* narrows down the search space by applying specific rules and constraints, making the solving process faster and more efficient.

Whether you are a beginner or an experienced puzzle solver, ʞᴉɯɥʇdᴉɹʞ's **versatile algorithms** make solving even the most challenging cryptarithms accessible and efficient.

## 📦 Dependencies

The library requires the following dependencies:

- Python 3.10 or higher
- SWI-Prolog 8.4.3 or higher (for constraint programming)

## 🗂️ Repository Structure

The repository is organized as follows:

```plaintext
├── crypthmik/
│   ├── solve
│   │   ├── __init__.py
│   │   ├── solver.py   
│   │   └── # other solver modules
│   └── utils
│       ├── __init__.py
│       ├── _cryptarithm.py
│       ├── _types.py
│       └── # other utility modules
├── README.md
├── LICENSE
└── requirements.txt
```

The `crypthmik` package contains the library's source code, including the solver and utility modules.

## 📥 Installation

To install the library, you can clone the repository and install the required dependencies using the following commands:

```bash
# Clone the repository
git clone https://github.com/Adhavane/cryptarithm-solver.git

# Navigate to the project directory
cd cryptarithm-solver

# Install the required dependencies
pip install -r requirements.txt
```

## 🚀 Usage

Here is an example of how to use the library to solve a cryptarithm:

```python
from crypthmik.utils import Cryptarithm
from crypthmik.solve import Enumerate, GenerateAndTest, ConstraintProgramming

# Define the cryptarithm
cryptarithm = Cryptarithm("HES + THE = BEST")

# Initialize the solvers
brute_force_solver = Enumerate()
generate_and_test_solver = GenerateAndTest()
constraint_solver = ConstraintProgramming()

# Solve the cryptarithm using different algorithms
for solver in [brute_force_solver, generate_and_test_solver, constraint_solver]:
    for solution in solver.solve(cryptarithm):
        print(f"Solution found by {solver.__class__.__name__}: {solution}")

# Output:
# Solution found by Enumerate: {'S': 6, 'E': 2, 'B': 1, 'T': 8, 'H': 4}
# Solution found by GenerateAndTest: {'H': 4, 'E': 2, 'S': 6, 'T': 8, 'B': 1}
# Solution found by ConstraintProgramming: {'H': 4, 'E': 2, 'S': 6, 'T': 8, 'B': 1}
```

## 📚 Documentation

### 📚🔠 Cryptarithm class

The [`Cryptarithm` class](/crypthmik/utils/_cryptarithm.py) represents a cryptarithm puzzle with an equation in the form of a string.

To create a `Cryptarithm` object, you can pass the equation as a string to the constructor:

```python
from crypthmik.utils import Cryptarithm

cryptarithm = Cryptarithm("SEND + MORE = MONEY")
```

The equation must be a valid arithmetic expression with the following rules:

```plaintext
EXPRESSION := TERM '=' TERM
TERM := WORD (OPERATOR WORD)*
WORD := [A-Z]+
OPERATOR := '+' | '-' | '*' | '/' | '%'
```

An `EXPRESSION` consists of two `TERM`s separated by the `=` operator. A `TERM` consists of one or more `WORD`s separated by an `OPERATOR`. A `WORD` is a sequence of one or more uppercase letters. An `OPERATOR` is one of the following: `+`, `-`, `*`, `/`, `%`.

The `/` operator represents integer division, and the `%` operator represents the modulo operation. For example, `10 / 3 = 3` and `10 % 3 = 1`.

```python
from crypthmik.utils import Cryptarithm

cryptarithm = Cryptarithm("FORTY + TEN + TEN = SIXTY")  # OK
cryptarithm = Cryptarithm("ABC * DE = HGBC")  # OK

cryptarithm = Cryptarithm("To be, or not to be")  # ERROR: Puzzle must contain exactly one equals sign.
cryptarithm = Cryptarithm("ODD + ODD == EVEN")  # ERROR: Invalid operator '=='. Use '=' instead.
```

By default, the `Cryptarithm` class treats the puzzle as case-insensitive, meaning it treats all letters as uppercase. However, it can be configured to be case-sensitive, treating uppercase and lowercase letters as distinct characters.

```python
from crypthmik.utils import Cryptarithm

# Create a Cryptarithm object with a case-insensitive puzzle
cryptarithm = Cryptarithm("lower + UPPER = case")
```

### 📚💡 Solution methods

The library provides three main solver classes to solve cryptarithms using different algorithms:

1. **Enumerate**: The [`Enumerate`](/crypthmik/solve/_enumerate.py) class implements a brute-force algorithm that systematically explore all possible solutions, ensuring none are missed. This method is simple but can be slow for large puzzles.
2. **GenerateAndTest**: The [`GenerateAndTest`](/crypthmik/solve/_generate_and_test.py) class uses a generate-and-test approach to iteratively generate potential solutions and test their validity. This method is more efficient than brute-force but still requires a significant amount of computation.
3. **ConstraintProgramming**: The [`ConstraintProgramming`](/crypthmik/solve/_constraint_programming.py) class leverages constraints to reduce the search space efficiently. This method is the most efficient and can solve complex puzzles quickly.

## 🤝 Contributing

This project is a **small**, **fun**, and **educational** endeavor to solve cryptarithm puzzles. It was created to develop my skills in Python and explore different problem-solving techniques.

If you would like **to contribute** to the project, feel free **to fork** the repository, make changes, and submit a **pull request**. Any contributions, bug fixes, or improvements are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

If you have any **questions**, **suggestions**, or **feedback**, feel free to reach out to me. I would love to hear from you!
