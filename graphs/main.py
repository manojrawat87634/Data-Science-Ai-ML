import matplotlib.pyplot as plt
import networkx as nx

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

G = nx.DiGraph()

for src, neighbors in roads.items():
    for dst, weight in neighbors.items():
        G.add_edge(src, dst, weight=weight)

pos = nx.spring_layout(G)

plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Road Network Graph (Directed)")
plt.tight_layout()
plt.show()