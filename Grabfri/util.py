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