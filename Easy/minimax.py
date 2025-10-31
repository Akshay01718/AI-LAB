def minimax(node, maximizing_player):
    if node not in graph or len(graph[node]) == 0:
        return value[node],[node]
    
    if maximizing_player:
        max_val=float('-inf')
        best_path=[]
        for child in graph[node]:
            eval, child_path =minimax(child,False)
            if eval > max_val:
                max_val= eval
                best_path = [node]+child_path
        return max_val, best_path
    else:
        min_val=float('inf')
        best_path=[]
        for child in graph[node]:
            eval, child_path=minimax(child, True)
            if eval < min_val:
                min_val= eval
                best_path = [node]+child_path
        return min_val,best_path

graph ={}
value={}
n=int(input("Enter the no.of nodes: "))

print("\nEnter the child nodes comma separated")
for _ in range(n):
    node = input("\nNode name: ").strip()
    children= input(f"children of {node}:" ).strip()
    if children=="":
        graph[node]=[]
    else:
        graph[node] = [x.strip() for x in children.split(",")]

print("Enter the heuristic value for leaf node")
for node in graph:
    if len(graph[node]) == 0:
        val=float(input(f"Enter the value of {node}: "))
        value[node]=val

root=input("Enter the root node: ")

result, best_path = minimax(root,True)
print("Best value for root: ",result)
print("Optimal path: ","->".join(best_path))