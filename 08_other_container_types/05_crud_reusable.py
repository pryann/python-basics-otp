def generate_id():
    return max(user["id"] for user in users) + 1


def get_all_users():
    return users

def find_user_by_id(id):
    for user in users:
        if user["id"] == id:
            return user


def update_user_by_id(id, update_user):
    user = find_user_by_id(id)
    if user is not None:
        index = users.index(user)
        users[index].update(update_user)
        return users[index]


def create_user(user):
    new_user = {"id": generate_id()}
    new_user.update(user)
    users.append(new_user)
    return users[-1]


def delete_user_by_id(id):
    user = find_user_by_id(id)
    if user is not None:
        users.remove(user)
        return user


