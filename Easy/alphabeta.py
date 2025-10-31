# --- Alpha-Beta Pruning with User Input ---

def alphabeta(node, alpha, beta, maximizingPlayer):
    global pruned_nodes
    # If leaf node
    if node not in graph or len(graph[node]) == 0:
        return values[node], [node]

    if maximizingPlayer:
        maxEval = float('-inf')
        best_path = []
        children=graph[node]
        for i, child in enumerate(children):
            eval, path = alphabeta(child, alpha, beta, False)
            if eval > maxEval:
                maxEval = eval
                best_path = [node] + path
            alpha = max(alpha, eval)
            if beta <= alpha:
                # Pruned remaining siblings
                pruned_nodes.extend(children[i+1:])
                break
        return maxEval, best_path
    else:
        minEval = float('inf')
        best_path = []
        children=graph[node]
        for i, child in enumerate(children):
            eval, path = alphabeta(child, alpha, beta, True)
            if eval < minEval:
                minEval = eval
                best_path = [node] + path
            beta = min(beta, eval)
            if beta <= alpha:
                pruned_nodes.extend(children[i+1:])
                break
        return minEval, best_path


# --- Input Section ---
graph = {}
values = {}
pruned_nodes=[]
n = int(input("Enter number of nodes: "))

print("\nEnter child nodes (comma separated) or leave blank for leaf nodes:")
for _ in range(n):
    node = input("\nNode name: ").strip()
    children = input(f"Children of {node}: ").strip()
    if children == "":
        graph[node] = []
    else:
        graph[node] = [x.strip() for x in children.split(",")]

print("\nEnter heuristic values for leaf nodes:")
for node in graph:
    if len(graph[node]) == 0:
        val = float(input(f"Value of {node}: "))
        values[node] = val

root = input("\nEnter root node: ").strip()

# --- Run Alpha-Beta Pruning ---
best_value, best_path = alphabeta(root, float('-inf'), float('inf'), True)

print("\nBest value at root:", best_value)
print("Optimal path:", " → ".join(best_path))
print("\nPruned edges: ",",".join(pruned_nodes) if pruned_nodes else "(none)")