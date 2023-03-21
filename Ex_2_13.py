import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Graphe a priori orienté : on utilise DiGraph à la place de Graph
G = nx.Graph()

# On crée les arêtes ; préremplissage possible avec :
# >>> [print(f"#{k}.\nG.add_edge(\"\", \"\", weight=)") for k in range(1,16)]
# Ext : extérieur

#1.
G.add_edge("Ext", "I", weight=6)
#2.
G.add_edge("Ext", "P1", weight=11)
#3.
G.add_edge("P1", "P2", weight=3)
#4.
G.add_edge("I", "P2", weight=5)
#5.
G.add_edge("P2", "P3", weight=2)
#6.
G.add_edge("P3", "Ext", weight=10)
#7.
G.add_edge("I", "At", weight=3)
#8.
G.add_edge("I", "P5", weight=4)
#9.
G.add_edge("P2", "Ad", weight=4)
#10.
G.add_edge("P4", "At", weight=5)
#11.
G.add_edge("At", "P5", weight=8)
#12.
G.add_edge("P5", "Ad", weight=5)
#13.
G.add_edge("Ext", "P4", weight=11)
#14.
G.add_edge("Ext", "At", weight=9)
#15.
G.add_edge("Ext", "P5", weight=11)
#16.
G.add_edge("Ext", "Ad", weight=4)


# On prépare le graphe pour l'affichage avec matplotlib
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
pos = nx.spring_layout(G, scale=1, dim=2)
nx.draw_networkx_nodes(G, pos, node_shape="o", node_size=1000, node_color="#00ff00")
nx.draw_networkx_labels(G, pos, font_size=12, font_color="#207020")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowsize=30, width=2, alpha=1, edge_color="#00a000")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), font_size=11, font_color="#008000")

# Exécution de l'algo de Kruskal, puis coloration des sommets parcourus + arêtes (zip)
T = nx.minimum_spanning_tree(G, weight="weight")
nx.draw_networkx_nodes(T, pos, nodelist=T.nodes(), node_shape="h", node_size=2000, node_color="#0033ff", alpha=0.3)
nx.draw_networkx_edges(G, pos, edgelist=T.edges(), edge_color="#0020a0", width=5, alpha=0.3)

# affichage avec matplotlib
plt.axis("off")
plt.tight_layout()
plt.show()

