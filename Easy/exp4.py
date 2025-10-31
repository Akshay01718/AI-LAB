from queue import PriorityQueue

# ------------------------
# Create Graph
# ------------------------
def create_graph():
    n = int(input("Enter total number of nodes: "))
    graph = {}
    heuristic = {}

    for i in range(n):
        node = input(f"Enter name of node {i+1}: ")
        h = int(input(f"Enter heuristic value of {node}: "))
        graph[node] = []
        heuristic[node] = h

    for node in graph:
        c = int(input(f"How many connections from {node}? "))
        for i in range(c):
            neighbor = input(f"Enter connected node to {node}: ")
            cost = int(input(f"Enter cost from {node} to {neighbor}: "))
            graph[node].append((neighbor, cost))

    return graph, heuristic


# ------------------------
# Print Graph
# ------------------------
def print_graph(graph, heuristic):
    print("\nGraph (Adjacency List):")
    for node, edges in graph.items():
        edge_str = ', '.join([f"{n}({c})" for n, c in edges]) or 'None'
        print(f"{node} (h={heuristic[node]}) --> {edge_str}")


# ------------------------
# Greedy Best First Search
# ------------------------
def greedy_best_first_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], [start]))
    visited = set()

    print("\nGreedy Best-First Search Traversal:")

    while not pq.empty():
        h, path = pq.get()
        node = path[-1]

        if node in visited:
            continue

        print(f"Visited: {node}")
        visited.add(node)

        if node == goal:
            print("Goal found!")
            print("Path:", " -> ".join(path))
            return

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], path + [neighbor]))

    print("Goal not reachable.")


# ------------------------
# A* Search
# ------------------------
def a_star_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, [start]))  # (f, g, path)
    visited = set()

    print("\nA* Search Traversal:")

    while not pq.empty():
        f, g, path = pq.get()
        node = path[-1]

        if node in visited:
            continue

        print(f"Visited: {node} | g={g} | f={f}")
        visited.add(node)

        if node == goal:
            print("Goal found!")
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                pq.put((f_new, g_new, path + [neighbor]))

    print("Goal not reachable.")


# ------------------------
# Main
# ------------------------
graph, heuristic = create_graph()
print_graph(graph, heuristic)

start = input("\nEnter starting node: ")
goal = input("Enter goal node: ")

while True:
    print("\n1. Greedy Best First Search")
    print("2. A* Search")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        greedy_best_first_search(graph, heuristic, start, goal)
    elif choice == '2':
        a_star_search(graph, heuristic, start, goal)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
