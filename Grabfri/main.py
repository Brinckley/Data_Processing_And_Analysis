import networkx as nx

from util import *

from graph import algo
from graph import drawer

  
def main():
    graph = json_to_dict_of_lists('friends_1.json') # small json file here
    # here all collected data should be written for further operations
    nxgraph = nx.from_dict_of_lists(graph)

    # drawing basic graph
    drawer.draw_graph(nxgraph, 'test_graph1.html')

    # calculating centers
    eigenvector_res_10 = algo.calc_by_eigenvector(nxgraph, 5)
    for eres in eigenvector_res_10:
        print("User name {} with value {}".format(eres[0], eres[1]))
    drawer.draw_graph_highlighted(nxgraph, eigenvector_res_10, 'eigenvector_highlighted1.html')

    closeness_res_10 = algo.calc_by_closeness(nxgraph, 5)
    for cres in closeness_res_10:
        print("User name {} {} ".format(cres[0].first_name, cres[0].last_name))
    drawer.draw_graph_highlighted(nxgraph, eigenvector_res_10, 'closeness_highlighted1.html')

    betweenness_res_10 = algo.calc_by_betweenness(nxgraph, 5)
    for bres in betweenness_res_10:
        print("User name {} {} ".format(bres[0].first_name, bres[0].last_name))
    drawer.draw_graph_highlighted(nxgraph, eigenvector_res_10, 'betweenness_highlighted1.html')


if __name__ == '__main__':
    main()
