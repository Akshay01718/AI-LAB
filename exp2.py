def vacuum(curr_loc, stateA, stateB):
    state = {
        "A": stateA,
        "B": stateB
    }

    cost = 0
    if curr_loc == 'A':
        other_loc = 'B'
    else:
        other_loc = 'A'

    if curr_loc == 'A':
        if state[curr_loc] == 1:  # dirty
            print("Room A is dirty")
            print("Room A is cleaned")
            cost += 1
            state[curr_loc] = 0  # clean

        print("Moving to Room B")
        cost += 1

        if state[other_loc] == 1:
            print("Room B is dirty")
            print("Room B is cleaned")
            state[other_loc] = 0
            cost += 1
            print("Moving to Room A")
            cost += 1
        else:
            print("Room B is already cleaned")
            print("Moving to Room A")
            cost += 1

        print("Final State\n Room A:", state["A"], ", Room B:", state["B"])

    elif curr_loc == 'B':
        other_loc = 'A'

        if state[curr_loc] == 1:  # dirty
            print("Room B is dirty")
            print("Room B is cleaned")
            cost += 1
            state[curr_loc] = 0  # clean

        print("Moving to Room A")
        cost += 1

        if state[other_loc] == 1:
            print("Room A is dirty")
            print("Room A is cleaned")
            state[other_loc] = 0
            cost += 1
            print("Moving to Room B")
            cost += 1
        else:
            print("Room A is already cleaned")
            print("Moving to Room B")
            cost += 1

        print("Final State\n Room A:", state["A"], ", Room B:", state["B"])

    print("Cost =", cost)


# Input from user
loc = input("Enter the location: ").upper()
A = int(input("A state (0 = Clean, 1 = Dirty): "))
B = int(input("B state (0 = Clean, 1 = Dirty): "))
vacuum(loc, A, B)
