import matplotlib.pyplot as plt
import networkx
from matplotlib import pylab
import networkx as nx
from pyvis import network as net


def draw_graph(networkx_graph, graph_title):
    pyvis_graph = net.Network(height="1000px", width="100%", bgcolor="#222222", font_color="white", notebook=True)
    pyvis_graph.repulsion()
    # for each node and its attributes in the networkx graph
    for node, node_attrs in networkx_graph.nodes(data=True):
        pyvis_graph.add_node(str(node), **node_attrs)

    # for each edge and its attributes in the networkx graph
    for source, target, edge_attrs in networkx_graph.edges(data=True):
        # if value/width not specified directly, and weight is specified, set 'value' to 'weight'
        if not 'value' in edge_attrs and not 'width' in edge_attrs and 'weight' in edge_attrs:
            # place at key 'value' the weight of the edge
            edge_attrs['value'] = edge_attrs['weight']
        # add the edge
        pyvis_graph.add_edge(str(source), str(target), **edge_attrs)
    # return and also save
    return pyvis_graph.show(graph_title)


def draw_graph_highlighted(networkx_graph: networkx.Graph, highlighted_nodes: list[str], graph_title: str):
    highlighted_nodes = [x[0] for x in highlighted_nodes]

    pyvis_graph = net.Network(height="1000px", width="100%", bgcolor="#222222", font_color="white", notebook=True)
    pyvis_graph.repulsion()

    # for each node and its attributes in the networkx graph
    for node, node_attrs in networkx_graph.nodes(data=True):
        if node in highlighted_nodes:
            pyvis_graph.add_node(str(node), color=' #FF0000', **node_attrs)
        else:
            pyvis_graph.add_node(str(node), **node_attrs)

    # for each edge and its attributes in the networkx graph
    for source, target, edge_attrs in networkx_graph.edges(data=True):
        # if value/width not specified directly, and weight is specified, set 'value' to 'weight'
        if not 'value' in edge_attrs and not 'width' in edge_attrs and 'weight' in edge_attrs:
            # place at key 'value' the weight of the edge
            edge_attrs['value'] = edge_attrs['weight']
        # add the edge
        pyvis_graph.add_edge(str(source), str(target), **edge_attrs)
    # return and also save
    return pyvis_graph.show(graph_title)
