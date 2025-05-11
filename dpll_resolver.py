import time

def unit_propagate(clauses, assignment):
    changed = True
    while changed:
        changed = False
        unit_clauses = [c for c in clauses if len(c) == 1]
        for unit in unit_clauses:
            lit = next(iter(unit))
            if -lit in assignment:
                return None, None
            if lit not in assignment:
                assignment.add(lit)
                new_clauses = []
                for clause in clauses:
                    if lit in clause:
                        continue
                    if -lit in clause:
                        reduced = set(clause)
                        reduced.remove(-lit)
                        if not reduced:
                            return None, None
                        new_clauses.append(frozenset(reduced))
                    else:
                        new_clauses.append(clause)
                clauses = new_clauses
                changed = True
    return clauses, assignment

def pure_literal_assign(clauses, assignment):
    literals = set(lit for clause in clauses for lit in clause)
    pure = set()
    for lit in literals:
        if -lit not in literals:
            pure.add(lit)
    for lit in pure:
        assignment.add(lit)
    new_clauses = [c for c in clauses if all(l not in c for l in pure)]
    return new_clauses, assignment

def dpll(clauses, assignment):
    clauses, assignment = unit_propagate(clauses, assignment)
    if clauses is None:
        return False

    clauses, assignment = pure_literal_assign(clauses, assignment)
    if not clauses:
        return True

    literals = set(lit for clause in clauses for lit in clause)
    var = next(iter(literals))

    new_assignment = assignment.copy()
    new_assignment.add(var)
    new_clauses = [c for c in clauses if var not in c]
    new_clauses = [frozenset(c - {-var}) for c in new_clauses]
    if dpll(new_clauses, new_assignment):
        return True

    new_assignment = assignment.copy()
    new_assignment.add(-var)
    new_clauses = [c for c in clauses if -var not in c]
    new_clauses = [frozenset(c - {var}) for c in new_clauses]
    return dpll(new_clauses, new_assignment)

def dpll_solver(clauses):
    clause_set = [frozenset(clause) for clause in clauses]
    result = dpll(clause_set, set())
    return result

def main():
    cnf = [[1, 2], [-1, 2]]

    start_time = time.time()
    result = dpll_solver(cnf)
    end_time = time.time()

    if result:
        print("SATISFIABLE")
    else:
        print("UNSATISFIABLE")

    print(f"Runtime: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()