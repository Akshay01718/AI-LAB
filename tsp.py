import itertools

def calculate_tour_cost(tour, distances):
    """Calculate total cost of a tour"""
    cost = 0
    for i in range(len(tour)):
        from_city = tour[i]
        to_city = tour[(i + 1) % len(tour)]  # Return to start
        cost += distances[(from_city, to_city)]
    return cost


def tsp_brute_force(cities, distances):
    """Find shortest tour by trying all possibilities"""
    start = cities[0]
    other_cities = cities[1:]
    
    best_tour = None
    best_cost = float('inf')
    
    # Try all possible orders
    for perm in itertools.permutations(other_cities):
        tour = [start] + list(perm)
        cost = calculate_tour_cost(tour, distances)
        
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    
    return best_tour, best_cost


# Input
num_cities = int(input("Enter number of cities: "))
cities = []

for i in range(num_cities):
    city = input(f"Enter city {i+1} name: ")
    cities.append(city)

# Get distances
distances = {}
print("\nEnter distances between cities:")

for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = int(input(f"Distance {cities[i]} to {cities[j]}: "))
        distances[(cities[i], cities[j])] = dist
        distances[(cities[j], cities[i])] = dist

# Solve TSP
print("\nSolving TSP...")
best_tour, best_cost = tsp_brute_force(cities, distances)

# Output
print("\n" + "="*40)
print("BEST TOUR FOUND:")
print("="*40)
print(" → ".join(best_tour) + f" → {best_tour[0]}")
print(f"\nTotal Distance: {best_cost}")
print("="*40)