users = [
    {"id": 1, "first_name": "Gerhardt", "last_name": "Franceschi", "email": "gfranceschi0@usa.gov"},
    {"id": 2, "first_name": "Zuzana", "last_name": "Demangel", "email": "zdemangel1@addtoany.com"},
    {"id": 3, "first_name": "Nikita", "last_name": "Gotmann", "email": "ngotmann2@boston.com"},
    {"id": 4, "first_name": "Mathian", "last_name": "Rigts", "email": "mrigts3@globo.com"},
    {"id": 5, "first_name": "Cyndie", "last_name": "Hoffman", "email": "choffman4@pbs.org"},
]

# CRUD: Create, Read, Update, Delete


def generate_id():
    return max(user["id"] for user in users) + 1


def get_all_users():
    return users


# print(get_all_users())


def find_user_by_id(id):
    # return next((user for user in users if user["id"] == id), None)
    for user in users:
        if user["id"] == id:
            return user
    return None


print(find_user_by_id(3))


def update_user_by_id(id, update_user):
    user = find_user_by_id(id)
    if user is not None:
        index = users.index(user)
        users[index].update(update_user)
        return users[index]
    # return None


print(update_user_by_id(3, {"first_name": "Kovács", "last_name": "Béla"}))


def create_user(user):
    new_user = {"id": generate_id()}
    new_user.update(user)
    users.append(new_user)
    # users.append({"id": generate_id(), **user})
    return users[-1]


print(create_user({"first_name": "John", "last_name": "Doe", "email": "jd@gmail.com"}))


# def delete_user_by_id(id):
#     user = find_user_by_id(id)
#     if user is None:
#         raise Exception("User not found")


def delete_user_by_id(id):
    user = find_user_by_id(id)
    if user is not None:
        users.remove(user)
        return user


print(delete_user_by_id(2))
