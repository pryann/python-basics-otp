yearly_salaries = [
    50_000,
    60_000,
    70_000,
    80_000,
]


print(len(yearly_salaries))

# concatenation
print([1, 2, 3] + [4, 5, 6])

# repetition
print([1, 2, 3] * 3)

# mutate
yearly_salaries[0] = 55_000
print(yearly_salaries)

# METHODS:
# append one element to the end of the list
yearly_salaries.append(90_000)
print(yearly_salaries)

# extend the list with another iterable
yearly_salaries.extend([100_000, 110_000])
print(yearly_salaries)

# insert an element at a specific index
yearly_salaries.insert(1, 59_990)
print(yearly_salaries)

# remove the first occurrence of an element, or raise ValueError if the element is not found
yearly_salaries.remove(59_990)
print(yearly_salaries)

# delete an element at a specific index, or raise IndexError if the index is out of range
del yearly_salaries[0]
print(yearly_salaries)

# remove element at a specific index (default the last element) and return it, or raise IndexError if the index is out of range
yearly_salaries.pop()
print(yearly_salaries)

# count the number of occurrences of an element in the list
print(yearly_salaries.count(80_000))

numbers = [3, 6, 7, 1, 55, 0, 1]
# sort the list, mutate the original  lsit
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

user = ["My", "name", "is", "John", "Doe"]
user_str = " | ".join(user)
print(user_str)
