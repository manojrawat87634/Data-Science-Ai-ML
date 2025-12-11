# roads = {
#     'House': {'A': 2, 'B': 5, 'C': 9},
#     'A': {'D': 4, 'C': 2},
#     'B': {'A': 1, 'E': 3},
#     'C': {'D': 2, 'F': 5},
#     'D': {'Library': 6, 'F': 2},
#     'E': {'D': 1, 'Library': 8},
#     'F': {'Library': 3},
#     'Library': {}
# }

# start = 'House'
# end = 'Library'

# # initialize distances
# shortest = {place: float('inf') for place in roads}
# shortest[start] = 0

# # to store the path
# previous = {place: None for place in roads}

# visited = set()

# while len(visited) < len(roads):
#     # pick unvisited node with smallest distance
#     current = None
#     current_dist = float('inf')
#     for place in shortest:
#         if place not in visited and shortest[place] < current_dist:
#             current = place
#             current_dist = shortest[place]
#     visited.add(current)

#     # update neighbors
#     for neighbor in roads[current]:
#         new_distance = shortest[current] + roads[current][neighbor]
#         if new_distance < shortest[neighbor]:
#             shortest[neighbor] = new_distance
#             previous[neighbor] = current   # store path

# # reconstruct path (backwards)
# path = []
# node = end
# while node is not None:
#     path.append(node)
#     node = previous[node]

# path.reverse()

# print("Shortest distance to Library:", shortest["Library"])
# print("Shortest path:", " -> ".join(path))


roads = {
    'House': {'A': 2, 'B': 5, 'C': 9},
    'A': {'D': 4, 'C': 2},
    'B': {'A': 1, 'E': 3},
    'C': {'D': 2, 'F': 5},
    'D': {'Library': 6, 'F': 2},
    'E': {'D': 1, 'Library': 8},
    'F': {'Library': 3},
    'Library': {}
}

start = "House"
end = "Library"

result_path = {}
for i in roads:
    result_path[i] = float("inf")

result_path[start] = 0
# print(result_path)

previous = {}
for i in roads:
    previous[i] = None


visited = set()
# print(previous)

while len(visited) < len(roads):
    current = None
    current_distance = float('inf')
    for place in result_path:
        if (place not in visited and result_path[place] < current_distance):
            current = place
            current_distance = result_path[place]
    visited.add(current)
    for neighbor in roads[current]:
        new_distance = current_distance + roads[current][neighbor]
        if new_distance < result_path[neighbor]:
            result_path[neighbor] = new_distance
            previous[neighbor] = current
    print(result_path)