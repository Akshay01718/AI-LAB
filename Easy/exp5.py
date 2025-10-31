from collections import deque

# 🎯 Goal (final solved board)
GOAL = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]  # 0 means the blank tile

# 🧩 Print the 3x3 board
def show_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()  # empty line for clarity

# 🧭 Find all possible moves (Up, Down, Left, Right)
def get_moves(board):
    moves = []
    zero = board.index(0)  # find blank position
    x, y = divmod(zero, 3) # convert index to row,col

    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    for move, (dx, dy) in directions.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_board = board.copy()
            # swap blank with new position
            new_board[zero], new_board[new_index] = new_board[new_index], new_board[zero]
            moves.append((new_board, move))
    return moves

# 🔍 BFS algorithm
def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        board, path = queue.popleft()

        if tuple(board) in visited:
            continue
        visited.add(tuple(board))

        if board == GOAL:
            return path  # found solution

        for next_board, move in get_moves(board):
            queue.append((next_board, path + [move]))

    return None  # no solution

# ▶️ Run the game
def main():
    print("Enter 9 numbers for the board (0 = blank):")
    start = list(map(int, input().split()))

    print("\nSolving the puzzle...\n")
    path = bfs(start)

    if path is None:
        print("❌ No solution found.")
        return

    print(f"✅ Puzzle solved in {len(path)} moves!\n")
    board = start

    for i, move in enumerate(path, start=1):
        board = [*apply_move(board, move)]
        print(f"Move {i}: {move}")
        show_board(board)

    print("🎯 Goal Reached!")
    print("Path:", " -> ".join(path))

# ♻️ Helper to apply a move (for printing steps)
def apply_move(board, move):
    zero = board.index(0)
    x, y = divmod(zero, 3)
    dx, dy = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}[move]
    new_x, new_y = x + dx, y + dy
    new_index = new_x * 3 + new_y
    new_board = board.copy()
    new_board[zero], new_board[new_index] = new_board[new_index], new_board[zero]
    return new_board


main()
