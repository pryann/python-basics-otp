# ordered,  allow duplicates, can contains different types,  IMMUTABLE

yearly_salaries = (100_000, 110_000, 120_000)

print(yearly_salaries)
print(yearly_salaries[0])
print(len(yearly_salaries))
print(yearly_salaries.count(110_000))
print(yearly_salaries.index(100_000))

rgb = (255, 0, 0)
coordinates = (47.497913, 19.040236)

# one element tuple
one_element_tupe = (42,)
print(type(one_element_tupe))


# return tuple
def calculate_statistics(numbers):
    return min(numbers), max(numbers)


print(calculate_statistics([1, 2, 3, 4, 5]))

# type decision: maybe wrong, use list instead of tuple if you need to change the values
rgb_list = list(rgb)
rgb_list[1] = 255
rgb = tuple(rgb_list)
