import random

def compute_tour_length(tour:list[int], adj_matrix:list[list[int]]):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities):
        j = (i + 1) % num_cities  # Next city in the tour
        total_distance += adj_matrix[tour[i]][tour[j]]
    return total_distance


def generate_random_route(num_cities:int):
    start = int(input("Start City? num/-1:"))
    random_ro = list(range(num_cities))
    random.shuffle(random_ro)
    if start!=-1:
        random_ro.remove(start)
        random_ro.insert(0,start)
    print("Initial route",random_ro)
    return random_ro    

def local_search_tsp(adj_matrix:list[list[int]]):
    g = int(0)
    num_cities = len(adj_matrix)
    current_tour = generate_random_route(num_cities)  # Initial tour, can start with any permutation
    
    best_tour = current_tour.copy()
    best_tour_length = compute_tour_length(best_tour, adj_matrix)

    improvement = True
    while improvement:
        g +=1
        improvement = False
        for i in range(1, num_cities - 1):
            for j in range(i + 1, num_cities):
                
                neighbor_tour = current_tour.copy()
                neighbor_tour[i], neighbor_tour[j] = neighbor_tour[j], neighbor_tour[i]
                neighbor_tour_length = compute_tour_length(neighbor_tour, adj_matrix)

                
                if neighbor_tour_length < best_tour_length:
                    current_tour = neighbor_tour.copy()
                    best_tour = current_tour.copy()
                    best_tour_length = neighbor_tour_length
                    print("Selected improved neighbour",current_tour)
                    improvement = True
                    break

            if improvement:
                break
    
    return best_tour, best_tour_length,g

adjacency_matrix = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

best_tour, best_tour_length ,total_steps= local_search_tsp(adjacency_matrix)
print("Best Tour:", best_tour)
print("Tour Length:", best_tour_length)
print("Total Steps:", total_steps)

