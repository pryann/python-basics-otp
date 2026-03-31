import crud_reusable as operations
from users import users

print(operations.get_all(users))
print(operations.find_by_id(users, 3))
