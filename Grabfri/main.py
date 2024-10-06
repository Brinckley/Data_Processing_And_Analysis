import time
import vk_api
import json
import os

import networkx as nx


existing_friends_dict = {}
friend_set = set()


class User:
    def __init__(self, data, user_id):
        self.id = data["id"] if "id" in data else data["friend_id"]
        self.user_id = user_id
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.is_closed = data["is_closed"] if "is_closed" in data else False
        self.data = {
            "user_id": user_id,
            "friend_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

        if "is_closed" in data:
            self.is_closed = data["is_closed"]
        else:
            self.is_closed = False

        if "is_deactivated" in data:
            self.is_closed = True

    def __str__(self):
        return json.dumps(self.data, ensure_ascii=False)

    def __repr__(self):
        return str(self)


def save_data(user_id, data):
    data = ",".join([str(fr) for fr in data])
    friend_set.add(user_id)

    with open(f"folder\\friends_{user_id}.json", "w", encoding="utf-8") as f:
        f.write(f"[{data}]")


def get_friends(vk, user_id):
    # print(f"get friends for {user_id}")
    if user_id in friend_set:
        return None

    if user_id in existing_friends_dict:
        return [User(json.loads(fr), user_id) for fr in existing_friends_dict[user_id]]

    friends = vk.friends.get(user_id=user_id, fields='domain')
    lst = [User(fr, user_id) for fr in friends["items"] if fr["first_name"] != "DELETED"]
    existing_friends_dict[user_id] = lst
    time.sleep(0.005)
    return lst


def parse_users(user_ids_filename):
    # Чтение моего айди
    with open(user_ids_filename) as file:
        base_users = [int(id) for id in file.readlines()]
    print("Base users ids : ", base_users)

    friends = []

    with open("token.txt") as file:
        access_token = file.readline()

    session = vk_api.VkApi(token=access_token)
    vk = session.get_api()

    for base_user in base_users:
        friends.extend(get_friends(vk, base_user))
        save_data(base_user, get_friends(vk, base_user))

    friends = list(set(friends))
    count_friends = len(friends)

    for i, friend in enumerate(friends):
        if not friend.is_closed:
            print(f"{friend.first_name} {friend.last_name} {i + 1}: {count_friends}")
            try:
                friends_of_friend = get_friends(vk, friend.id)

                if not friends_of_friend:
                    continue

                save_data(friend.id, friends_of_friend)

                count_friends_of_friend = len(friends_of_friend)
                for j, friend_of_friends in enumerate(friends_of_friend):
                    print(
                        f"\t{friend_of_friends.first_name} {friend_of_friends.last_name} {j + 1}: {count_friends_of_friend}")
                    try:
                        friend3_lvl = get_friends(vk, friend_of_friends.id)

                        if not friend3_lvl:
                            continue

                        save_data(friend_of_friends.id, friend3_lvl)

                        del friend3_lvl
                    except:
                        print("\tUser banned")

                del friends_of_friend
            except:
                print("User banned")


def read_json_to_dict(json_file):
    with open(json_file) as json_file:
        data = json.load(json_file)
    return nx.from_dict_of_lists(data)


def calc_by_eigenvector(graph):
    eigenvector_centers = list(nx.eigenvector_centrality(graph).items())
    sorted_items = sorted(eigenvector_centers, key=lambda i: i[1], reverse=True)
    return sorted_items


def calc_by_closeness(graph):
    closeness_centers = list(nx.closeness_centrality(graph).items())
    sorted_items = sorted(closeness_centers, key=lambda i: i[1], reverse=True)
    return sorted_items


def calc_by_betweenness(graph):
    betweenness_centers = list(nx.betweenness_centrality(graph).items())
    sorted_items = sorted(betweenness_centers, key=lambda i: i[1], reverse=True)
    return sorted_items



def main():
    group_ids = ['168420440', '50933461',  '198216820', '220523027']
    # parse_users("user_ids.txt")

    nxgraph = read_json_to_dict("full_dataset.json")

    print("Calculating closeness eigenvector of graph")
    eigenvector_res = calc_by_eigenvector(nxgraph)
    print("Сloseness eigenvector of graph calculated ...")
    for eres in eigenvector_res:
        if eres[0] in group_ids:
            print("User name {} with value {}".format(eres[0], eres[1]))

    print("Calculating closeness centrality of graph")
    closeness_res = calc_by_closeness(nxgraph)
    print("Сloseness centrality of graph calculated ...")
    for cres in closeness_res:
        if cres[0] in group_ids:
            print("User name {} with value {}".format(cres[0], cres[1]))


    print("Calculating betweenness centrality of graph")
    betweenness_res = calc_by_betweenness(nxgraph)
    print("Сloseness betweenness of graph calculated ...")
    for bres in betweenness_res:
        if bres[0] in group_ids:
            print("User name {} with value {}".format(bres[0], bres[1]))




if __name__ == '__main__':
    main()