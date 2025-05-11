import time

def resolve_clauses(c1, c2):
    for literal in c1:
        if -literal in c2:
            new_clause = set(c1).union(c2)
            new_clause.discard(literal)
            new_clause.discard(-literal)
            if any(-lit in new_clause for lit in new_clause):
                return None
            return frozenset(new_clause)
    return None

def resolution_solver(clauses):
    clause_set = set(frozenset(clause) for clause in clauses)
    new = set()

    while True:
        clause_list = list(clause_set)
        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                c1, c2 = clause_list[i], clause_list[j]
                resolvent = resolve_clauses(c1, c2)
                if resolvent is not None:
                    if not resolvent:
                        return False  
                    new.add(resolvent)

        if new.issubset(clause_set):
            return None  

        clause_set.update(new)
        new.clear()

def main():
    cnf = [[1], [-1]]
    start_time = time.time()
    result = resolution_solver(cnf)
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