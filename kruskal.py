import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def random_graph(nodes:int=6, edges:int=12, weight:int=20, directed=False) -> nx.classes.graph.Graph :
    """Build a random nx graph or digraph"""
    edges = min(edges, nodes*(nodes-1)//2)
    nodes_list = [chr(el) for el in range(65, 65+nodes)]
    edges_list = random.sample([(x, y, random.randint(1, weight)) for x in nodes_list for y in nodes_list if x<y], edges)
    if directed :
        G = nx.DiGraph()
    else :
        G = nx.Graph()
    G.add_nodes_from(nodes_list)
    G.add_weighted_edges_from(edges_list)
    return G

def algo_dijkstra(G:nx.classes.graph.Graph, start_node=None, end_node=None) -> tuple :
    """Returns the shortests path from a node to other nodes in a connex component"""
    """PAS FINI"""
    if start_node is None :
        start_node = G.nodes()[0]
    inf = float("inf")
    connex_nodes = nx.node_connected_component(G, start_node)

    paths_table = {node : (node, 0 if node==start_node else inf) for node in sorted(G.nodes())}
    pass
    
def algo_kruskal(G:nx.classes.graph.Graph) -> tuple :
    """Returns the minimal covering tree of a non-oriented graph"""
    
    # 1st part : sorting the edges by weight (increasing)
    edges_weighted = sorted(G.edges(data="weight"), key=lambda x:x[2])
    
    # 2nd part : keep the edges that are not included in a connex component :
    connex_component = {node : node for node in sorted(G.nodes())}
    keep_edges = []
    total_weight = 0
    # for : in case of a non-connex graph (we get a covering tree for each connex component)
    for edge in edges_weighted :
        x, y, w = min(edge[:2]), max(edge[:2]), edge[2]
        if connex_component[x] != connex_component[y] :
            print("edge",x,y,w)
            print("before",connex_component)
            representative = min(connex_component[x], connex_component[y])
            node_merged = max(connex_component[x], connex_component[y])
            for node in connex_component.keys() :
                if connex_component[node] == node_merged :
                    connex_component[node] = representative
            print("after ",connex_component)
            keep_edges.append(edge)
            total_weight += w
    # nx graph build
    T = nx.Graph()
    T.add_weighted_edges_from(keep_edges)
    return T, total_weight

def draw_graph(ls:list) -> None :
    """display a graph with matplotlib"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 9))
    if not isinstance(ls, list) :
        ls = [ls]
    pos = nx.spring_layout(ls[0], scale=1, dim=2)
    for el in ls :
        color1 = '#'+''.join([hex(random.randint(42,220))[2:] for _ in range(3)])
        color2 = '#'+''.join([hex(random.randint(16,32))[2:] for _ in range(3)])
        nx.draw_networkx_nodes(el, pos, node_shape="o", node_size=1000, alpha=1, node_color=color1)
        nx.draw_networkx_labels(el, pos, font_size=12, font_color=color2)
        if nx.is_directed(el) :
            nx.draw_networkx_edges(el, pos, edgelist=el.edges(), arrowsize=30, width=2, alpha=1, edge_color=color1)
        else :
            nx.draw_networkx_edges(el, pos, edgelist=el.edges(), width=2, alpha=1, edge_color=color1)
        nx.draw_networkx_edge_labels(el, pos, edge_labels=nx.get_edge_attributes(el, "weight"), font_size=11, font_color=color2)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    G = random_graph(nodes=6, edges=12)
    T, w = algo_kruskal(G)
    print(f"Total weight : {w}")
    rep = ""
    while not rep :
        draw_graph([G, T])
        rep = input("Redraw ? ")


