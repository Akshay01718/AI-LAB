import itertools

# Function to calculate total distance of a route
def get_total_distance(route, distance_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    total += distance_matrix[route[-1]][route[0]]  # Return to start
    return total

# Function to solve TSP using brute force
def tsp_bruteforce(cities, distance_matrix):
    start = 0  # Always start from first city
    other_cities = list(range(1, len(cities)))

    best_route = None
    best_distance = float('inf')

    # Try all possible orders of other cities
    for perm in itertools.permutations(other_cities):
        route = [start] + list(perm)
        total_distance = get_total_distance(route, distance_matrix)

        if total_distance < best_distance:
            best_distance = total_distance
            best_route = route

    return best_route, best_distance

# ---------------- Main Program ----------------

print("=== Traveling Salesman Problem (Brute Force) ===")
num = int(input("Enter number of cities: "))

# Get city names
cities = []
for i in range(num):
    name = input(f"Enter name of city {i + 1}: ")
    cities.append(name)

# Get distance matrix
print("\nEnter distances between cities:")
distance_matrix = [[0] * num for _ in range(num)]

for i in range(num):
    for j in range(i + 1, num):
        dist = int(input(f"Distance from {cities[i]} to {cities[j]}: "))
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist

# Solve TSP
print("\nSolving TSP...\n")
best_route, best_distance = tsp_bruteforce(cities, distance_matrix)

# Display result

print("Best Route Found:")
for i in best_route:
    print(cities[i], end=" → ")
print(cities[best_route[0]])  # Return to start

print(f"\nTotal Distance: {best_distance}")

