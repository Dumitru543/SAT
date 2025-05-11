import time

def unit_propagate(clauses):
    assignment = set()
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
                changed = True
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
    return clauses, assignment

def dp_solver(clauses):
    clause_set = [frozenset(clause) for clause in clauses]
    assignment = set()

    while clause_set:
        clause_set, unit_assign = unit_propagate(clause_set)
        if clause_set is None:
            return False
        assignment |= unit_assign

        vars_in_clauses = set(abs(lit) for clause in clause_set for lit in clause)
        if not vars_in_clauses:
            return None 

        var = next(iter(vars_in_clauses))
        pos_clauses = [c for c in clause_set if var in c]
        neg_clauses = [c for c in clause_set if -var in c]
        others = [c for c in clause_set if var not in c and -var not in c]

        new_clauses = set()
        for pc in pos_clauses:
            for nc in neg_clauses:
                resolvent = (pc | nc) - {var, -var}
                if not resolvent:
                    return False  
                if any(-lit in resolvent for lit in resolvent):
                    continue  
                new_clauses.add(frozenset(resolvent))

        clause_set = others + list(new_clauses)

    return None   

def main():
  
    cnf = [[1, -2], [2], [-1]]

    start_time = time.time()
    result = dp_solver(cnf)
    end_time = time.time()

    if result is False:
        print("UNSATISFIABLE")
    elif result is None:
        print("INCONCLUSIVE")
    else:
        print("SATISFIABLE")  

    print(f"Runtime: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()