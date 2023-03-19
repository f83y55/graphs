import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Graphe a priori orienté : on utilise DiGraph à la place de Graph
G = nx.DiGraph()

# On crée les arêtes ; préremplissage possible avec :
# >>> [print(f"#{k}.\nG.add_edge(\"\", \"\", weight=)") for k in range(1,19)]

#1.
G.add_edge("Départ", "Marché", weight=4)
#2.
G.add_edge("Départ", "Forêt", weight=1)
#3.
G.add_edge("Forêt", "Marché", weight=2)
#4.
G.add_edge("Forêt", "Capitale", weight=7)
#5.
G.add_edge("Marché", "Col du Nord", weight=5)
#6.
G.add_edge("Marché", "Capitale", weight=3)
#7.
G.add_edge("Col du Nord", "Refuge du devin", weight=3)
#8.
G.add_edge("Capitale", "Refuge du devin", weight=4)
#9.
G.add_edge("Capitale", "Palais du roi", weight=10)
#10.
G.add_edge("Refuge du devin", "Épée", weight=20)
#11.
G.add_edge("Refuge du devin", "Grotte du dragon", weight=32)
#12.
G.add_edge("Refuge du devin", "Palais du roi", weight=5)
#13.
G.add_edge("Palais du roi", "Cartes", weight=6)
#14.
G.add_edge("Cartes", "Trésor", weight=30)
#15.
G.add_edge("Cartes", "Épée", weight=7)
#16.
G.add_edge("Épée", "Grotte du dragon", weight=8)
#17.
G.add_edge("Épée", "Trésor", weight=18)
#18.
G.add_edge("Grotte du dragon", "Trésor", weight=9)


# On prépare le graphe pour l'affichage avec matplotlib
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
pos = nx.spring_layout(G, scale=1, dim=2)
nx.draw_networkx_nodes(G, pos, node_shape="o", node_size=1000, node_color="#00ff00")
nx.draw_networkx_labels(G, pos, font_size=12, font_color="#207020")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowsize=30, width=2, alpha=1, edge_color="#00a000")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), font_size=11, font_color="#008000")

# Exécution de l'algo de Dijkstra, puis coloration des sommets parcourus + arêtes (zip)
shortest_path = nx.dijkstra_path(G, source="Départ", target="Trésor", weight="weight")
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_shape="h", node_size=2000, node_color="#0033ff", alpha=0.3)
shortest_path_edges = list( zip(shortest_path, shortest_path[1:]) )
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color="#0020a0", width=5, alpha=0.3)

# affichage avec matplotlib
plt.axis("off")
plt.tight_layout()
plt.show()

