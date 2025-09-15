import networkx as nx
import matplotlib.pyplot as plt

def is_valid(node, color, assignment, graph):
    """Check if assigning color to node is valid (CSP constraint)"""
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, nodes, graph, colors):
    """Backtracking CSP solver"""
    if len(assignment) == len(nodes):
        return assignment

    node = [n for n in nodes if n not in assignment][0]

    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, nodes, graph, colors)
            if result:
                return result
            del assignment[node]

    return None

num_nodes = int(input("Enter number of nodes: "))
nodes = []

for i in range(num_nodes):
    node_name = input(f"Enter name for node {i+1}: ")
    nodes.append(node_name)

graph = {node: [] for node in nodes}

print("\nNow enter connections for each node :")
for node in nodes:
    neighbors = input(f"Enter nodes connected to {node}: ").split()
    for neighbor in neighbors:
        if neighbor in nodes and neighbor != node:
            graph[node].append(neighbor)

for u in graph:
    for v in graph[u]:
        if u not in graph[v]:
            graph[v].append(u)

colors = input("\nEnter available colors : ").split()

print("\nCSP Formulation :")
print("Variables (Nodes) :", nodes)
print("Domain (Colors) :", colors)
print("Constraints: Adjacent nodes must not share the same color")
for u in graph:
    for v in graph[u]:
        if nodes.index(u) < nodes.index(v):
            print(f"{u} != {v}")

solution = backtrack({}, nodes, graph, colors)

print("\nGraph :", graph)
if solution:
    print("\nSolution (Node : Assigned Color)")
    for node, color in solution.items():
        print(f"{node} : {color}")

    G = nx.Graph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)

    node_colors = [solution[node] for node in G.nodes]

    plt.figure(figsize=(6, 6))
    nx.draw(
        G,
        with_labels=True,
        node_color=node_colors,
        node_size=1000,
        font_size=12,
        font_color="white",
        edge_color="black"
    )
    plt.show()
else:
    print("No solution found with given colors.")
