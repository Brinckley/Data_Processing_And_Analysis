import time
import vk_api
import matplotlib.pyplot as plt
from matplotlib import pylab
import networkx as nx

import util
from util import *
from user import User

from graph import algo
from graph import drawer


def get_friends(vk, user_id):
    friends = vk.friends.get(user_id=user_id, fields='domain')
    lst = [User(fr) for fr in friends["items"]]
    print(lst)
    time.sleep(0.005)
    return lst


def main():
    base_users = read_ids_from_file('user_ids.txt')
    print("Base users ids : ", base_users)

    auth_token = util.parse_token('token.txt')
    session = vk_api.VkApi(token=auth_token)
    vk = session.get_api()

    graph = {}
    friends = []

    for base_user in base_users:
        friends.extend(get_friends(vk, base_user))

    friends = set(friends)
    for friend in friends:
        print('Processing', "\tid: ", friend.id,
              "\tName : ", friend.first_name, friend.last_name)
        if friend.first_name == "DELETED":
            continue

        if not friend.is_closed:
            try:
                all_friends = get_friends(vk, friend.id)
                mutual = []

                for i in all_friends:
                    for j in friends:
                        if i.id == j.id:
                            mutual.append(j)

                graph[friend] = list(set(mutual))
            except:
                print("User banned")
        else:
            graph[friend] = list()

    # here all collected data should be written for further operations
    nxgraph = nx.from_dict_of_lists(graph)
    #
    # drawing basic graph
    drawer.draw_graph(nxgraph, 'test_graph1.html')
    #
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
