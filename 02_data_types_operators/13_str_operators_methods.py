print("Hello " + "world")
print("Hello" * 3)
print(len("Hello"))
name = "John"
print(name[0])
print(name[1])
print(name[-1])

# TypeError: 'str' object does not support item assignment
#  str is immutable
# name[0] = "j"

name = "janea"
print(type(name))
print("capitalized:", name.capitalize())
print(name)

name = name.capitalize()
print(name)

print("uppercase:", name.upper())
print("lowercase:", name.lower())
print("isLower:", name.islower())
print("find index 'a':", name.find("a"))
print("count of 'a':", name.count("a"))
print("replace 'a' with 'A':", name.replace("a", "A"))
print("remove leading and trailing whitespace characters:", "  Gergely      ".strip())
