import networkx as nx
import matplotlib.pyplot as plt

# Check if assigning 'color' to 'node' is valid
def is_valid(node, color, graph, colors_assigned):
    for neighbor in graph[node]:
        if colors_assigned.get(neighbor) == color:
            return False
    return True

# Backtracking algorithm
def color_graph(graph, nodes, colors, colors_assigned):
    if len(colors_assigned) == len(nodes):  # All nodes colored
        return colors_assigned

    node = [n for n in nodes if n not in colors_assigned][0]

    for color in colors:
        if is_valid(node, color, graph, colors_assigned):
            colors_assigned[node] = color  # Try color
            result = color_graph(graph, nodes, colors, colors_assigned)
            if result:
                return result
            del colors_assigned[node]  # Backtrack

    return None

# ---------------------------
# MAIN PROGRAM
# ---------------------------
num = int(input("Enter number of nodes: "))
nodes = []
for i in range(num):
    node = input(f"Enter name for node {i+1}: ")
    nodes.append(node)

# Create graph (dictionary)
graph = {n: [] for n in nodes}

print("\nEnter neighbors for each node (space-separated):")
for node in nodes:
    neighbors = input(f"{node}: ").split()
    for n in neighbors:
        if n in nodes and n != node:
            graph[node].append(n)
            graph[n].append(node)  # Make it undirected

# Get color options
colors = input("\nEnter color options (space-separated): ").split()

# Solve
solution = color_graph(graph, nodes, colors, {})

# Show result
if solution:
    print("\n✅ Coloring Solution:")
    for n, c in solution.items():
        print(f"{n} → {c}")

    # Visualize
    G = nx.Graph(graph)
    node_colors = [solution[n] for n in G.nodes]
    nx.draw(G, with_labels=True, node_color=node_colors,
            node_size=1000, font_color="white", font_weight="bold")
    plt.show()
else:
    print("\n❌ No valid coloring found with given colors.")
