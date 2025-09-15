from queue import PriorityQueue

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.connections = []
        self.visited = False

    def add_connection(self, node, cost):
        self.connections.append((node, cost))


def create_graph():
    nodes = {}
    nodes_num = int(input("Enter total number of nodes: "))

    for i in range(nodes_num):
        name = input(f"Enter node {i+1} name: ")
        heuristic = int(input(f"Enter heuristic value for node {name}: "))
        nodes[name] = Node(name, heuristic)

    for name in nodes:
        conn_num = int(input(f"How many nodes connected to {name}? "))
        for i in range(conn_num):
            conn_name = input(f"Enter node connected to {name}: ")
            cost = int(input(f"Enter cost from {name} to {conn_name}: "))
            if conn_name in nodes:
                nodes[name].add_connection(nodes[conn_name], cost)
            else:
                print(f"Node '{conn_name}' does not exist! Skipping...")

    return nodes


def print_graph(nodes):
    for name, node in nodes.items():
        connections = [(n.name, cost) for n, cost in node.connections]
        print(f"{name} (h={node.heuristic}) is connected to {connections}")


def greedy_best_first_search(start, goal):
    for node in nodes.values():
        node.visited = False

    pq = PriorityQueue()
    # (heuristic, cost_so_far, node, path)
    pq.put((start.heuristic, 0, start, []))

    while not pq.empty():
        h, cost_so_far, current, path = pq.get()

        if current.visited:
            continue

        current.visited = True
        path = path + [current.name]
        print(f"Visited: {current.name} | Cost so far: {cost_so_far}")

        if current.name == goal.name:
            print("Goal node found!")
            print("Path:", " -> ".join(path))
            print("Total cost:", cost_so_far)
            return

        for neighbor, cost in current.connections:
            if not neighbor.visited:
                pq.put((neighbor.heuristic, cost_so_far + cost, neighbor, path))

    print("Goal not reachable")


def a_star_search(start, goal):
    for node in nodes.values():
        node.visited = False

    pq = PriorityQueue()
    # (f = g + h, g, node, path)
    pq.put((start.heuristic, 0, start, []))

    while not pq.empty():
        f, g, current, path = pq.get()

        if current.visited:
            continue

        current.visited = True
        path = path + [current.name]
        print(f"Visited: {current.name} | g={g} | f={f}")

        if current.name == goal.name:
            print("Goal node found!")
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return

        for neighbor, cost in current.connections:
            if not neighbor.visited:
                g_new = g + cost
                f_new = g_new + neighbor.heuristic
                pq.put((f_new, g_new, neighbor, path))

    print("Goal not reachable")


nodes = create_graph()
print_graph(nodes)

start_name = input("\nEnter starting node: ")
goal_name = input("Enter goal node: ")

while True:
    print("\nChoose Search Algorithm:")
    print("1 Greedy Best First Search")
    print("2 A* Search")
    print("3 Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        greedy_best_first_search(nodes[start_name], nodes[goal_name])
    elif choice == 2:
        a_star_search(nodes[start_name], nodes[goal_name])
    elif choice == 3:
        break
    else:
        print("Invalid choice")
