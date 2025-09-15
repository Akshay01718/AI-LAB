from collections import deque

GOAL_STATE = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    x, y = divmod(zero_index, 3)
    moves = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}

    for move, (dx, dy) in moves.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = state.copy()
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append((new_state, move))
    return neighbors

def bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        state_tuple = tuple(current_state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current_state == GOAL_STATE:
            return path

        for neighbor, move in get_neighbors(current_state):
            if tuple(neighbor) not in visited:
                queue.append((neighbor, path + [move]))

    return None

def apply_move(state, move):
    zero_index = state.index(0)
    x, y = divmod(zero_index, 3)
    moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    dx, dy = moves[move]
    new_x, new_y = x + dx, y + dy
    new_index = new_x * 3 + new_y
    new_state = state.copy()
    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
    return new_state

def main():
    raw_input_state = input("Enter the initial state (9 numbers from 0-8 separated by space, 0 = blank): ")
    initial_state = list(map(int, raw_input_state.strip().split()))

    print("\nStarting BFS...\n")
    solution_path = bfs(initial_state)

    if solution_path is None:
        print("Goal not reachable")
        return

    current_state = initial_state
    for i, move in enumerate(solution_path, start=1):
        current_state = apply_move(current_state, move)
        print(f"Move #{i}: {move}")
        print_board(current_state)

    print("Goal Reached!!")
    print("Path:", " -> ".join(solution_path))
    print("Total Moves:", len(solution_path))

if __name__ == "__main__":
    main()
