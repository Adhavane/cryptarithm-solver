# .ʞᴉɯɥʇdʎɹɔ 🧩🧠

## 📜 Table of Contents

- [🔍 Overview](#-overview)
- [📦 Dependencies](#-dependencies)
- [🗂️ Repository Structure](#️-repository-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📫 Contact](#-contact)

## 🔍 Overview

ʞᴉɯɥʇdʎɹɔ is a simple and easy-to-use Python library designed for effortlessly solving cryptarithms with just a few lines of code.

Cryptarithms, also known as [alphametics](https://en.wikipedia.org/wiki/Verbal_arithmetic), are puzzles where digits are replaced by letters of the alphabet. The goal is to find the correct mapping of letters to digits to make a valid arithmetic equation. For example, in the cryptarithm `SEND + MORE = MONEY`, each letter represents a unique digit, and the task is to find the correct assignment of digits to letters to make the equation true.

The library provides several algorithms to tackle these puzzles, including brute-force, generate-and-test, and constraint programming methods. The *[brute-force method](https://en.wikipedia.org/wiki/Enumeration_algorithm)* involves exhaustively enumerating all possible combinations to find a solution. The *[generate-and-test](https://en.wikipedia.org/wiki/Trial_and_error)* approach iteratively generates potential solutions and tests their validity. Meanwhile, *[constraint programming](https://en.wikipedia.org/wiki/Constraint_programming)* narrows down the search space by applying specific rules and constraints, making the solving process faster and more efficient.

Whether you are a beginner or an experienced puzzle solver, ʞᴉɯɥʇdʎɹɔ's versatile algorithms make solving even the most challenging cryptarithms accessible and efficient.

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

📥 Installation

To install the library, you can clone the repository and install the required dependencies using the following commands:

```bash
# Clone the repository
git clone https://github.com/Adhavane/cryptarithm-solver.git

# Navigate to the project directory
cd cryptarithm-solver

# Install the required dependencies
pip install -r requirements.txt
```

🚀 Usage

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

## 🤝 Contributing

This project is a small, fun, and educational endeavor to solve cryptarithm puzzles. It was created to develop my skills in Python and explore different problem-solving techniques.

If you would like to contribute to the project, feel free to fork the repository, make changes, and submit a pull request. Any contributions, bug fixes, or improvements are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

If you have any questions, suggestions, or feedback, feel free to reach out to me. I would love to hear from you!
