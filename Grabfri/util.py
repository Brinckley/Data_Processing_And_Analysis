import json
from user import User
import vk_api
import time


def read_ids_from_file(file_name):
    user_file = open(file_name, 'r')
    count = 0

    user_ids = []
    while True:
        count += 1
        line = user_file.readline()
        if not line:
            break
        user_ids.append(int(line))
    user_file.close()
    return user_ids


def parse_token(token_file_name):
    toke_file = open(token_file_name, 'r')
    return toke_file.readline()


def save_users_to_json(user, friends, filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    users_data = [
        {
            "user_id": user,
            "friend_id": friend.id,
            "first_name": friend.first_name,
            "last_name": friend.last_name
        }
        for friend in friends
    ]

    existing_data.extend(users_data)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)


def get_friends(vk, user_id):
    print(f"get friends for {user_id}")
    friends = vk.friends.get(user_id=user_id, fields='domain')
    lst = [User(fr) for fr in friends["items"]]
    print(lst)
    time.sleep(0.005)
    return lst


def parse_friends_to_file(base_users_file_name):
    with open("user_ids.txt") as file:
        base_users = [int(id) for id in file.readlines()]
    # base_users = read_ids_from_file('user_ids.txt')
    print("Base users ids : ", base_users)
    filename = f'friends_{base_users[0]}.json'

    access_token = ""
    with open("config.txt") as file:
        access_token = file.readline()

    session = vk_api.VkApi(token=access_token)
    vk = session.get_api()

    graph = {}
    friends = []

    for base_user in base_users:
        friends.extend(get_friends(vk, base_user))
    save_users_to_json(base_user, friends, filename)

    friends = set(friends)
    for friend in friends:
        #print('Processing', "\tid: ", friend.id,
        #      "\tName : ", friend.first_name, friend.last_name)
        if friend.first_name == "DELETED":
            continue

        if not friend.is_closed:
            try:
                friends_of_friends = []
                friends_of_friends.extend(get_friends(vk, friend.id))
                save_users_to_json(friend.id, friends_of_friends, filename)
                friends_of_friends = set(friends_of_friends)
                mutual = []

                for i in friends_of_friends:
                    for j in friends:
                        if i.id == j.id:
                            mutual.append(j)

                graph[friend] = list(set(mutual))

                for friend_of_friend in friends_of_friends:
                    #print('Processing', "\tid: ", friend_of_friend.id,
                    #      "\tName : ", friend_of_friend.first_name, friend_of_friend.last_name)
                    if friend_of_friend.first_name == "DELETED":
                        continue

                    if not friend_of_friend.is_closed:
                        try:
                            all_friends = get_friends(vk, friend_of_friend.id)
                            save_users_to_json(friend_of_friend.id, all_friends, filename)
                            mutual0 = []

                            for i in all_friends:
                                for j in friends_of_friends:
                                    if i.id == j.id:
                                        mutual0.append(j)

                            graph[friend_of_friend] = list(set(mutual0))
                        except:
                            print("User banned")
                    else:
                        graph[friend_of_friend] = list()

            except:
                print("User banned")
        else:
            graph[friend] = list()


def json_to_dict_of_lists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

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
