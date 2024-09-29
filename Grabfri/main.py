
import time
import vk_api
import matplotlib.pyplot as plt
from matplotlib import pylab
import networkx as nx
import json
from collections import defaultdict

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

  
def json_to_dict_of_lists(file_path):
    # Открываем JSON файл и считываем данные
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Создаем словарь, где ключи - это user_id, а значения - списки множеств друзей
    result = {}
    all_friends = []

    for entry in data:
        friend_info = User({
            "id": entry['friend_id'],
            "first_name": entry['first_name'],
            "last_name": entry['last_name'],
            "domain": 'id' + str(entry['friend_id'])
        })

        all_friends.append(friend_info)

    
    for entry in data:
        user_info = {
            "id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "is_closed": False,
            "domain": "id"
        }

        # Создание объекта User
        tmp = User(user_info)
        for friend in all_friends:
            if entry['user_id'] == friend.id:
                tmp = friend
        tmp_friends = []
        for entry in data:
            for friend in all_friends:
                if entry['friend_id'] == friend.id:
                    tmp_friends.append(friend)
        result[tmp] = list(set(tmp_friends))

    return result

  
def main():
    graph = json_to_dict_of_lists('friends_1.json')

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
