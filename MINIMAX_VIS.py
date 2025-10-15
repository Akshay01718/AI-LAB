import math
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name, value=None):
        self.name = name    
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        
    def is_leaf(self):
        return not self.children

def build_tree_recursive(parent_name, nodes):
    try:
        num_children_input = input(f"Enter the number of children for node '{parent_name}' (or leave blank for a leaf node): ").strip()
        
        if num_children_input == "":
            print(f"Node '{parent_name}' is considered a leaf node.")
            return

        num_children = int(num_children_input)
        if num_children < 0:
            print("Number of children cannot be negative. Please try again.")
            build_tree_recursive(parent_name, nodes)
            return

        for i in range(num_children):
            child_name = input(f"Enter the name of child {i+1} for '{parent_name}': ").strip()
            
            new_child = Node(child_name)
            nodes[child_name] = new_child
            nodes[parent_name].add_child(new_child)
            
            build_tree_recursive(child_name, nodes)

    except ValueError:
        print("Invalid input. Please enter an integer or leave blank.")
        build_tree_recursive(parent_name, nodes)

def assign_leaf_values(node):
    if node.is_leaf():
        while True:
            try:
                value = int(input(f"Enter the value for leaf node '{node.name}': "))
                node.value = value
                break
            except ValueError:
                print("Invalid value. Please enter an integer.")
    else:
        for child in node.children:
            assign_leaf_values(child)

def build_tree():
    print("--- Tree Structure Input ---")
    nodes = {}
    
    root_name = input("Enter the name of the root node: ").strip()
    root = Node(root_name)
    nodes[root_name] = root
    
    build_tree_recursive(root_name, nodes)
        
    print("\n--- Assigning Leaf Node Values ---")
    assign_leaf_values(root)
    
    return root

def minimax(node, is_max_turn):
    if node.is_leaf():
        print(f"Leaf node '{node.name}' has value {node.value}")
        return node.value, [node.name]

    if is_max_turn:
        print(f"Maximizing player at node '{node.name}'")
        best_value = -math.inf
        best_path = []
        for child in node.children:
            value, path = minimax(child, False)
            if value > best_value:
                best_value = value
                best_path = [node.name] + path
        print(f"  --> Node '{node.name}' chooses max value: {best_value}")
        return best_value, best_path
    else:
        print(f"Minimizing player at node '{node.name}'")
        best_value = math.inf
        best_path = []
        for child in node.children:
            value, path = minimax(child, True)
            if value < best_value:
                best_value = value
                best_path = [node.name] + path
        print(f"  --> Node '{node.name}' chooses min value: {best_value}")
        return best_value, best_path

def alpha_beta_pruning(node, is_max_turn, alpha, beta, pruned_edges=None):
    if pruned_edges is None:
        pruned_edges = []

    if node.is_leaf():
        print(f"  Leaf node '{node.name}' has value {node.value}")
        return node.value, [node.name], pruned_edges

    if is_max_turn:
        print(f"\nMaximizer at '{node.name}' (Alpha: {alpha}, Beta: {beta})")
        best_value = -math.inf
        best_path = []
        children = node.children
        for i, child in enumerate(children):
            value, path, pruned_edges = alpha_beta_pruning(child, False, alpha, beta, pruned_edges)
            if value > best_value:
                best_value = value
                best_path = [node.name] + path
            alpha = max(alpha, best_value)
            print(f"  After visiting '{child.name}', new Alpha: {alpha}")
            if beta <= alpha:
                print(f"  Pruning branch at '{child.name}' as Beta ({beta}) <= Alpha ({alpha})")
                # Add all siblings after current child as pruned
                for pruned_child in children[i+1:]:
                    pruned_edges.append((node.name, pruned_child.name))
                break
        return best_value, best_path, pruned_edges
    else:
        print(f"\nMinimizer at '{node.name}' (Alpha: {alpha}, Beta: {beta})")
        best_value = math.inf
        best_path = []
        children = node.children
        for i, child in enumerate(children):
            value, path, pruned_edges = alpha_beta_pruning(child, True, alpha, beta, pruned_edges)
            if value < best_value:
                best_value = value
                best_path = [node.name] + path
            beta = min(beta, best_value)
            print(f"  After visiting '{child.name}', new Beta: {beta}")
            if beta <= alpha:
                print(f"  Pruning branch at '{child.name}' as Beta ({beta}) <= Alpha ({alpha})")
                # Add all siblings after current child as pruned
                for pruned_child in children[i+1:]:
                    pruned_edges.append((node.name, pruned_child.name))
                break
        return best_value, best_path, pruned_edges

def build_nx_graph(node, graph=None):
    if graph is None:
        graph = nx.DiGraph()
    graph.add_node(node.name, value=node.value)
    for child in node.children:
        graph.add_edge(node.name, child.name)
        build_nx_graph(child, graph)
    return graph

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if root is None:
        root = list(nx.topological_sort(G))[0]

    def _hierarchy_pos(G, root, left, right, vert_loc, pos):
        pos[root] = ((left + right) / 2, vert_loc)
        children = list(G.successors(root))
        if len(children) != 0:
            dx = (right - left) / len(children)
            nextx = left
            for child in children:
                next_right = nextx + dx
                _hierarchy_pos(G, child, nextx, next_right, vert_loc - vert_gap, pos)
                nextx += dx

    pos = {}
    _hierarchy_pos(G, root, 0, width, vert_loc, pos)
    return pos

def draw_graph_with_path_and_pruning(graph, optimal_path, pruned_edges):
    pos = hierarchy_pos(graph, root=optimal_path[0])

    plt.figure(figsize=(12,8))
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=1500)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')

    node_labels = {node: f"{graph.nodes[node]['value']}" if graph.nodes[node]['value'] is not None else "" for node in graph.nodes}
    label_pos = {k: (v[0], v[1] - 0.05) for k, v in pos.items()}
    nx.draw_networkx_labels(graph, label_pos, labels=node_labels, font_size=10, font_color='red')

    # Draw all edges in default color first
    nx.draw_networkx_edges(graph, pos, arrows=True)

    # Highlight optimal path edges in orange
    path_edges = list(zip(optimal_path, optimal_path[1:]))
    nx.draw_networkx_nodes(graph, pos, nodelist=optimal_path, node_color='orange', node_size=1800)
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='orange', width=3, arrows=True)

    # Highlight pruned edges in red
    nx.draw_networkx_edges(graph, pos, edgelist=pruned_edges, edge_color='red', style='dashed', width=2, arrows=True)

    plt.title("Game Tree with Optimal Path (orange) and Pruned Edges (red)", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    root = build_tree()
    print("\nTree building complete.")

    while True:
        print("\n--- Menu ---")
        print("1. Run Minimax Algorithm")
        print("2. Run Alpha-Beta Pruning Algorithm")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            print("\n--- Running Minimax Algorithm ---")
            optimal_value, optimal_path = minimax(root, True)
            print(f"\nOptimal value from Minimax: {optimal_value}")
            print(f"Optimal path: {' -> '.join(optimal_path)}")

            graph = build_nx_graph(root)
            draw_graph_with_path_and_pruning(graph, optimal_path, pruned_edges=[])  # No pruning in minimax

        elif choice == '2':
            print("\n--- Running Alpha-Beta Pruning Algorithm ---")
            optimal_value, optimal_path, pruned_edges = alpha_beta_pruning(root, True, -math.inf, math.inf)
            print(f"\nOptimal value from Alpha-Beta Pruning: {optimal_value}")
            print(f"Optimal path: {' -> '.join(optimal_path)}")
            print(f"Pruned edges: {pruned_edges}")

            graph = build_nx_graph(root)
            draw_graph_with_path_and_pruning(graph, optimal_path, pruned_edges)

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
