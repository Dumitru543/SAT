# SAT Solver Algorithm Comparison

This repository compares three algorithms for solving propositional satisfiability (SAT) problems:

- **Resolution**
- **Davis-Putnam (DP)**
- **Davis-Putnam-Logemann-Loveland (DPLL)**

Each algorithm was implemented and run against a set of test cases. Results include satisfiability status and runtime.

## Summary Table

| Test # | CNF Formula                                                                 | Resolution         | DP                 | DPLL               |
|--------|------------------------------------------------------------------------------|--------------------|--------------------|--------------------|
| 1      | `[[1], [-1]]`                                                               | UNSAT (0.000008s)  | UNSAT (0.000011s)  | UNSAT (0.000008s)  |
| 2      | `[[1, 2], [-1, 2]]`                                                         | SAT (0.000020s)    | INC (0.000018s)    | SAT (0.000015s)    |
| 3      | `[[1, 2], [3, 4]]`                                                          | INC (0.000015s)    | INC (0.000016s)    | SAT (0.000016s)    |
| 4      | `[[1, 2], [-1], [-2], [3], [-3, 4], [-4]]`                                   | UNSAT (0.000046s)  | UNSAT (0.000013s)  | UNSAT (0.000013s)  |
| 5      | `[[1, 2], [3, 4], [5, 6], [1, 3], [2, 4], [5, -6]]`                          | INC (0.000047s)    | INC (0.000028s)    | SAT (0.000021s)    |
| 6      | `[[1, 2, 3], [-1, 4], [2, 5], [-3, 6], [4, 7], [5, -8], [-6, 9], ...]`       | INC (0.000775s)    | INC (0.000284s)    | SAT (0.000092s)    |

> Test 6 full CNF (truncated in table for readability):
```text
[[1, 2, 3], [-1, 4], [2, 5], [-3, 6], [4, 7], [5, -8], [-6, 9],
 [7, 10], [-8, 11], [9, -12], [-10, 13], [11, 14], [-12, 15],
 [13, -16], [-14, 17], [15, -18], [-16, 19], [17, -20], [18, 21],
 [-19, 22], [20, 23], [21, -24], [22, 25], [23, 26], [-24, 27]]
