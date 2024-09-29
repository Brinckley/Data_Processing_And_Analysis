import json
from user import User


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
