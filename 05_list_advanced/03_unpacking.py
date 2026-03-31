from numpy import number


first_name = "John"
last_name = "Doe"
age = 30


first_name, last_name, age = "John", "Doe", 30


# data swapping
a = 10
b = 20

a, b = b, a
print("a:", a)
print("b:", b)
# tmp = b
# b = a
# a = tmp

# unpacking string
abc = "abc"
a, b, c = abc
print(a, b, c)

# unpacking list
user = ["John", "Doe", 30]
first_name, last_name, age = user
print(first_name, last_name, age)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, *_ = numbers
print(first, second)

first, *_, last = numbers
print(first, last)
