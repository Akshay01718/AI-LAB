class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False

    def add_connection(self, node):
        self.connections.append(node)

def create_graph():
    NodesNum = int(input("Enter the total number of nodes: "))
    nodes = {}

    for i in range(NodesNum):
        node_name = input(f"Enter node {i+1} value: ")
        nodes[node_name] = Node(node_name)

    for node_name in nodes:
        count = int(input(f"How many nodes are connected to {node_name}? "))
        for i in range(count):
            conn_name = input(f"Enter the name of the node connected to {node_name}: ")
            if conn_name in nodes:
                nodes[node_name].add_connection(nodes[conn_name])
            else:
                print(f"Node '{conn_name}' does not exist! Skipping.")
    return nodes

def print_graph(nodes):
    print("\nAdjacency List of the graph:")
    for node_name, node in nodes.items():
        connections = [n.name for n in node.connections]
        print(f"{node_name}: {', '.join(connections)}")

def dfs(start_node, destination_node):
    stack = [start_node]
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node.name in visited:
            continue
        visited.add(current_node.name)
        print(f"Visited {current_node.name}")

        if current_node.name == destination_node.name:
            print("Destination node found!")
            return

        for neighbor in current_node.connections:
            if neighbor.name not in visited:
                stack.append(neighbor)
    print("Destination node not found.")

def bfs(start_node, destination_node):
    queue = [start_node]
    visited = set()

    while queue:
        current_node = queue.pop(0)
        if current_node.name in visited:
            continue
        visited.add(current_node.name)
        print(f"Visited {current_node.name}")

        if current_node.name == destination_node.name:
            print("Destination node found!")
            return

        for neighbor in current_node.connections:
            if neighbor.name not in visited:
                queue.append(neighbor)
    print("Destination node not found.")

nodes = create_graph()
print_graph(nodes)

start = input("\nEnter starting node: ")
destination = input("Enter destination node: ")

stop = True
while(stop):
    choice = int(input("\nEnter \n1. BFS\n2. DFS\n3. Exit\nYour choice: "))

    if choice == 1:
        bfs(nodes[start], nodes[destination])
    elif choice == 2:
        dfs(nodes[start], nodes[destination])
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid Choice!")
