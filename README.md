# SAT Solvers - Resolution, DP, DPLL

This repository contains Python implementations of three SAT solving algorithms:

- **Resolution**
- **Davis–Putnam (DP)**
- **Davis–Putnam–Logemann–Loveland (DPLL)**

These algorithms solve SAT (Satisfiability) problems expressed in Conjunctive Normal Form (CNF).
Each script assumes the input CNF formula is represented as a list of lists of integers, e.g., [[1, -2], [2], [-1, 3]], which corresponds to 
(x₁ ∨ ¬x₂) ∧ (x₂) ∧ (¬x₁ ∨ x₃)
The repository also includes a set of results from running these solvers that were covered in the paper.

---

##  Setup and Usage

To run the SAT solvers on a CNF formula, simply execute the desired solver script.

### Running a Solver:

1. Clone or download the repository.
2. Ensure Python 3.8 or higher is installed on your system.
3. Place your CNF formula as a list of clauses (e.g., `[[1, -2], [2], [-1]]`).
