metros = {
    "Rajiv Chowk": {"Barakhamba Road": 1.0, "Netaji Subhash Place": 2.0},
    "Barakhamba Road": {"Mandi House": 1.0},
    "Mandi House": {"Pragati Maidan": 1.5},
    "Pragati Maidan": {"Indraprastha": 1.2},
    "Indraprastha": {"Yamuna Bank": 1.8},
    "Yamuna Bank": {"Noida Sector 15": 2.3},
    "Noida Sector 15": {"Noida Sector 16": 1.0},
    "Noida Sector 16": {"Noida Sector 18": 1.2},
    "Noida Sector 18": {"Noida City Centre": 1.5},
    "Noida City Centre": {"Golf Course": 1.8},
    "Golf Course": {"Botanical Garden": 1.0},
    "Botanical Garden": {"Laxmi Nagar": 2.0},
    "Laxmi Nagar": {"Preet Vihar": 1.4},
    "Preet Vihar": {"Karkarduma": 1.6},
    "Karkarduma": {"Anand Vihar ISBT": 1.2},
    "Anand Vihar ISBT": {"Kaushambi": 1.7},
    "Kaushambi": {"Vaishali": 1.8},
    "Vaishali": {"Yamuna Bank": 3.0},  # loop back
    "Netaji Subhash Place": {"Model Town": 1.3},
    "Model Town": {"GTB Nagar": 1.7},
    "GTB Nagar": {"Vishwavidyalaya": 1.5},
    "Vishwavidyalaya": {"Civil Lines": 1.2},
    "Civil Lines": {"Kashmere Gate": 1.1},
    "Kashmere Gate": {"Chandni Chowk": 1.2},
    "Chandni Chowk": {"Chawri Bazar": 0.9},
    "Chawri Bazar": {"New Delhi": 1.0},
    "New Delhi": {"Patel Chowk": 1.4},
    "Patel Chowk": {"Central Secretariat": 0.8},
    "Central Secretariat": {"AIIMS": 2.3},
    "AIIMS": {"Green Park": 1.5},
    "Green Park": {"Hauz Khas": 1.7},
    "Hauz Khas": {"Malviya Nagar": 1.5},
    "Malviya Nagar": {"Saket": 2.0},
    "Saket": {"Qutub Minar": 1.8},
    "Qutub Minar": {"Chhattarpur": 2.0},
    "Chhattarpur": {"Sultanpur": 2.5},
    "Sultanpur": {"Ghitorni": 1.8},
    "Ghitorni": {"Arjan Garh": 2.0},
    "Arjan Garh": {"Guru Dronacharya": 1.9},
    "Guru Dronacharya": {"Sikanderpur": 2.2},
    "Sikanderpur": {"MG Road": 1.3},
    "MG Road": {"IFFCO Chowk": 1.6},
    "IFFCO Chowk": {"HUDA City Centre": 2.1},
    "HUDA City Centre": {"IFFCO Chowk": 2.1},  # single track loop
    "Dwarka Sector 21": {"Dwarka Sector 14": 1.3},
    "Dwarka Sector 14": {"Dwarka Sector 13": 1.1},
    "Dwarka Sector 13": {"Dwarka Sector 12": 1.0},
    "Dwarka Sector 12": {"Dwarka Sector 11": 0.9},
    "Dwarka Sector 11": {"Dwarka Sector 10": 1.0},
    "Dwarka Sector 10": {"Dwarka Sector 9": 1.2},
    "Dwarka Sector 9": {"Dwarka Sector 8": 1.3},
    "Dwarka Sector 8": {"Dwarka Sector 21": 3.5},
}
# metros = {
#     'House': {'A': 2, 'B': 5, 'C': 9},
#     'A': {'D': 4, 'C': 2},
#     'B': {'A': 1, 'E': 3},
#     'C': {'D': 2, 'F': 5},
#     'D': {'Library': 6, 'F': 2},
#     'E': {'D': 1, 'Library': 8},
#     'F': {'Library': 3},
#     'Library': {}
# }
start = input("Enter starting station: ")
end = input("Enter ending station: ")

if start not in metros or end not in metros:
    print("Invalid start or end station.")
    exit()

# initialize distances
shortest = {place: float('inf') for place in metros}
shortest[start] = 0

# to store the path
previous = {place: None for place in metros}

visited = set()

while len(visited) < len(metros):
    # pick unvisited node with smallest distance
    current = None
    current_dist = float('inf')
    for place in shortest:
        if place not in visited and shortest[place] < current_dist:
            current = place
            current_dist = shortest[place]
    if current is None:
        break  # no reachable node left
    visited.add(current)

    # update neighbors
    for neighbor in metros[current]:
        new_distance = shortest[current] + metros[current][neighbor]
        if new_distance < shortest[neighbor]:
            shortest[neighbor] = new_distance
            previous[neighbor] = current   # store path

# reconstruct path (backwards)
path = []
node = end
while node is not None:
    path.append(node)
    node = previous[node]

path.reverse()

print("Shortest distance to", end, ":", shortest[end])
print("Shortest path:", " -> ".join(path))