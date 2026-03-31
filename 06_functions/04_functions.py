# def is_even_number(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# def is_even_number(number):
#     if number % 2 == 0:
#         return "even"
#     return "odd"

# ternary operator
# def is_even_number(number):
#     return "even" if number % 2 == 0 else "odd"


def is_even_number(number):
    return number % 2 == 0


print(is_even_number(4))
print(is_even_number(7))

# recursive function
def gcd(a, b):
    # if b == 0:
    #     return a
    # else:
    #     return gcd(b, a % b)
    print("fn called with a =", a, "and b =", b)
    return a if b == 0 else gcd(b, a % b)


# print(gcd(11, 33))
print(gcd(110, 3342))
