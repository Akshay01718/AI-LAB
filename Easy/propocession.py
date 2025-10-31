# ----------------------------------------
# Simple Logic Inference Program
# Supports: Modus Ponens, Modus Tollens, and Unit Resolution
# ----------------------------------------
from collections import deque

# ---------- MODUS PONENS ----------
def modus_ponens(implication, premise):
    parts = implication.lower().split(",")
    if len(parts) != 2 or "if" not in parts[0]:
        return "Invalid format! Use: 'If P, Q'"

    first = parts[0].replace("if", "").strip()
    second = parts[1].strip()

    if premise.lower() == first:
        return f"Therefore, {second} (Modus Ponens)"
    return "Premise doesn't match the condition."


# ---------- MODUS TOLLENS ----------
def modus_tollens(implication, neg_consequent):
    parts = implication.lower().split(",")
    if len(parts) != 2 or "if" not in parts[0]:
        return "Invalid format! Use: 'If P, Q'"

    first = parts[0].replace("if", "").strip()
    second = parts[1].strip()

    if not neg_consequent.lower().startswith("not "):
        return "Please write negation like: 'Not Q'"

    given_consequent = neg_consequent.lower().replace("not ", "").strip()

    if given_consequent == second:
        return f"Therefore, not {first} (Modus Tollens)"
    return "Consequent doesn't match."


# ---------- UNIT RESOLUTION ----------
def resolve_clauses(c1, c2):
    result = set(c1)
    for lit in c2:
        if -lit in result:
            result.remove(-lit)
        else:
            result.add(lit)
    return tuple(sorted(result))

def resolution_solver(clauses):
    queue = deque(clauses)
    while len(queue) > 1:
        first = queue.popleft()
        second = queue.popleft()
        new_clause = resolve_clauses(first, second)
        if not new_clause:
            return "Result: Contradiction (empty clause)"
        if len(new_clause) == 1:
            return f"Result: Resolved to: {new_clause[0]}"
        queue.appendleft(new_clause)
    return f"Result: Final clause: {queue[0]}"


# ---------- MAIN PROGRAM ----------
while True:
    print("\n=== LOGIC INFERENCE SYSTEM ===")
    print("1. Modus Ponens")
    print("2. Modus Tollens")
    print("3. Unit Resolution")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        imp = input("Enter implication (e.g., 'If it rains, ground is wet'): ")
        pre = input("Enter known fact (e.g., 'it rains'): ")
        print(modus_ponens(imp, pre))

    elif choice == "2":
        imp = input("Enter implication (e.g., 'If it rains, ground is wet'): ")
        neg = input("Enter negated consequent (e.g., 'Not ground is wet'): ")
        print(modus_tollens(imp, neg))

    elif choice == "3":
        print("Enter your clauses as a list of tuples (e.g., [(1, -2), (-1, 3)])")
        clauses = eval(input("Clauses: "))
        print(resolution_solver(clauses))

    elif choice == "4":
        print("👋 Exiting program...")
        break

    else:
        print("⚠️ Invalid choice! Please enter 1, 2, 3, or 4.")
