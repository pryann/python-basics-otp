# list is a collection of ordered
# list is mutable
# allow duplicate elements
# can contain elements of different types
# vat = 27
# standard_hungarian_vat_in_percent = 27

yearly_salaries = [
    50_000,
    60_000,
    70_000,
    80_000,
]

# ordered
print(yearly_salaries[0])
print(yearly_salaries[1])

# mutable
yearly_salaries[0] = 55_000
print(yearly_salaries)

# allow duplicate elements, and different types
user = ["John", "Doe", 30, ["reading", "coding"], True, True]
