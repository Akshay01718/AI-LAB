import random
import networkx as nx
import matplotlib.pyplot as plt

colors = ['red', 'green', 'blue']

# Count the number of conflicts in current coloring
def count_conflicts(graph, coloring):
    conflicts = 0
    for node in graph:
        for neighbor in graph[node]:
            if coloring[node] == coloring[neighbor]:
                conflicts += 1
    return conflicts // 2  # Each edge counted twice

# Try changing each node's color to reduce conflicts
def get_best_neighbor(graph, coloring):
    current_conflicts = count_conflicts(graph, coloring)
    best_coloring = coloring.copy()
    improved = False

    for node in graph:
        original_color = coloring[node]
        for color in colors:
            if color != original_color:
                new_coloring = coloring.copy()
                new_coloring[node] = color
                new_conflicts = count_conflicts(graph, new_coloring)
                if new_conflicts < current_conflicts:
                    print(f"Changing color of node {node} from {original_color} to {color}")
                    current_conflicts = new_conflicts
                    best_coloring = new_coloring
                    improved = True
    return best_coloring, improved

# Hill Climbing main function
def hill_climb(graph):
    coloring = {node: random.choice(colors) for node in graph}
    print("Initial Coloring:", coloring)
    steps = 0

    while True:
        coloring, improved = get_best_neighbor(graph, coloring)
        steps += 1
        if not improved:
            break

    print(f"\nTotal steps: {steps}")
    print("Final Coloring:", coloring)
    return coloring

# Draw the graph with assigned colors
def draw_graph(graph, coloring):
    G = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    node_colors = [coloring.get(node, 'gray') for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=600, font_weight='bold')
    plt.show()

# ----------------------------
# MAIN PROGRAM (simplified)
# ----------------------------
print("=== Graph Coloring using Hill Climbing ===")
print("Colors used: Red, Green, Blue")
print("Enter graph as a dictionary (e.g., {0:[1,2], 1:[0,2], 2:[0,1]})")

user_input = input("Graph: ")
graph = eval(user_input)  # assuming input will always be valid

final_coloring = hill_climb(graph)
draw_graph(graph, final_coloring)
