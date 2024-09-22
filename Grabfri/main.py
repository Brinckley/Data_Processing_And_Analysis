import time
import vk_api
import scipy
import matplotlib.pyplot as plt
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

                graph[friend] = mutual
            except:
                print("User banned")
        else:
            graph[friend] = list()

    g = nx.from_dict_of_lists(graph)

    options = {
        'node_color': 'red',
        'node_size': 40,
        'font_size': 12,
        # 'with_labels': True,
        'font_color': 'black',
        'style': 'solid',
    }

    nx.draw_spring(g, **options)
    plt.show()


if __name__ == '__main__':
    main()
