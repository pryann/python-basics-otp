yearly_salaries = [
    50_000,  # 0
    60_000,  # 1
    70_000,  # 2
    80_000,  # 3
]

print(50_000 in yearly_salaries)  # True
print(90_000 in yearly_salaries)  # False

bool_value = True
print(bool_value, type(bool_value))  # True <class 'bool'>


price = 10_000
licit = int(input("Enter your bid: "))
print(price > licit)
