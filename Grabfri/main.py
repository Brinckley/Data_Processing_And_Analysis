import time
import vk_api
import scipy
import matplotlib.pyplot as plt
from matplotlib import pylab
import networkx as nx

import util
from user import User
from util import *


def get_friends(vk, user_id):
    friends = vk.friends.get(user_id=user_id, fields='domain')
    lst = [User(fr) for fr in friends["items"]]
    print(lst)
    time.sleep(0.005)
    return lst


def save_graph(graph,file_name):
    plt.figure(num=None, figsize=(120, 120), dpi=80)
    plt.axis('off')
    fig = plt.figure(1)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_labels(graph,pos)

    cut_x = 1.50
    cut_y = 1.50
    xmax = cut_x * max(xx for xx, yy in pos.values())
    ymax = cut_y * max(yy for xx, yy in pos.values())
    plt.xlim(-xmax, xmax)
    plt.ylim(-ymax, ymax)

    plt.savefig(file_name,bbox_inches="tight")
    pylab.close()
    del fig


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

    g = nx.from_dict_of_lists(graph)
    save_graph(g, "my_graph.png")


if __name__ == '__main__':
    main()
