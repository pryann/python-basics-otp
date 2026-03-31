# store key value pairs
# ordered
# mutable
# no duplicate keys

user = {"name": "John Doe", "age": 30}
print(user["name"])

user["name"] = "Jane Doe"
print(user)

# add a new key value pair
user["email"] = "email.address@domain.com"
print(user)

# remove a key value pair
user.pop("age")
print(user)

user.update({"age": 18, "name": "John Doedoe"})
print(user)

for value in user:
    print(value)

keys = user.keys()
print(type(keys))
# AttributeError: 'dict_keys' object has no attribute 'pop'
# print(keys.pop())
# if you want to call list methods, you need to convert it to a list first
print(list(keys))

for value in user.values():
    print(value)

for key, value in user.items():
    print(key, value)
