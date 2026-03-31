# Minimum kiválasztás
def get_minimum(values):
    # use input check in real life scenarios
    # if not values or len(values) == 0:
    #     return None

    # works only if values is not empty
    # min_value = values[0]
    # for i in range(1, len((values))):
    #     if values[i] < min_value:
    #         min_value = values[i]
    # return min_value

    min_value = float("inf")

    for value in values:
        if value < min_value:
            min_value = value

    return min_value


values = [1, 2, 3, 4, 5, 6, 7]
print(get_minimum(values))
print(min(values))


# Maximum kiválasztás
def get_maximum(values):
    max_value = float("-inf")

    for value in values:
        if value > max_value:
            max_value = value

    return max_value


print(get_maximum(values))
print(max(values))


#  Összegzés
def summa(values):
    total = 0
    for value in values:
        total += value
    return total


print(summa(values))
print(sum(values))


def average(values):
    # total = 0
    # for value in values:
    #     total += value
    # return total / len(values)
    return summa(values) / len(values)


print(average(values))
print(sum(values) / len(values))


# Megszámlálás
def count_values(values, search):
    count = 0
    for value in values:
        if value == search:
            count += 1
    return count


print(count_values(values, 3))
print(values.count(3))


# Kiválasztás - tudjuk, hogy benne van az elem, kell az indexe
def get_index(values: list[int], element: int) -> int | None:
    for index, value in enumerate(values):
        if value == element:
            return index
    # return None


print(get_index(values, 3))
print(values.index(3))


# Eldöntés - True/False
def is_contains(values, search):
    for value in values:
        if value == search:
            return True
    return False


print(is_contains(values, 3))
print(3 in values)
