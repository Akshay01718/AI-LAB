from collections import deque


def create_graph():
    n = int(input("Enter number of nodes: "))
    graph = {}

    for _ in range(n):
        node = input("Enter node name: ")
        connections = input(f"Enter nodes connected to {node} (comma-separated): ").split(',')
        graph[node] = [c for c in connections if c]
    return graph

def print_graph(graph):
    print("\nGraph (Adjacency List):")
    for node, neighbors in graph.items():
        print(f"{node} --> {', '.join(neighbors) if neighbors else 'None'}")

        
def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}  # Track where each node came from
    print("\nBFS Traversal:")

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        print(f"Visited: {node}")
        if node == goal:
            print("Destination found!")
            # 🔁 Reconstruct the path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            print("Path:", " -> ".join(reversed(path)))
            return
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    print("Destination not found.")

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    parent = {start: None}
    print("\nDFS Traversal:")

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(f"Visited: {node}")
        if node == goal:
            print("Destination found!")
            # 🔁 Reconstruct the path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            print("Path:", " -> ".join(reversed(path)))
            return
        visited.add(node)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                stack.append(neighbor)
    print("Destination not found.")

# ------------------------
# Main
# ------------------------
graph = create_graph()
print_graph(graph)

start = input("\nEnter starting node: ")
goal = input("Enter destination node: ")

while True:
    print("\n1. BFS\n2. DFS\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        bfs(graph, start, goal)
    elif choice == '2':
        dfs(graph, start, goal)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
