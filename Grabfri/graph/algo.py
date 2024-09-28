import networkx as nx


def calc_by_eigenvector(graph, num):
    print("Calculating closeness eigenvector of graph")
    eigenvector_centers = list(nx.eigenvector_centrality(graph).items())
    sorted_items = sorted(eigenvector_centers, key=lambda i: i[1], reverse=True)
    return sorted_items[:num]


def calc_by_closeness(graph, num):
    print("Calculating closeness centrality of graph")
    eigenvector_centers = list(nx.closeness_centrality(graph).items())
    sorted_items = sorted(eigenvector_centers, key=lambda i: i[1], reverse=True)
    return sorted_items[:num]


def calc_by_betweenness(graph, num):
    print("Calculating betweenness centrality of graph")
    eigenvector_centers = list(nx.betweenness_centrality(graph).items())
    sorted_items = sorted(eigenvector_centers, key=lambda i: i[1], reverse=True)
    return sorted_items[:num]