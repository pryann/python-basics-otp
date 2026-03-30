yearly_salaries = [
    50_000,  # 0
    60_000,  # 1
    70_000,  # 2
    80_000,  # 3
]

for yearly_salary in yearly_salaries:
    print(yearly_salary)

for i in range(len(yearly_salaries)):
    print(f"index: {i}, value: {yearly_salaries[i]}")

# enumerate: i is not a real index, but a counter that starts from 0 and increments by 1 for each iteration
for index, yearly_salary in enumerate(yearly_salaries):
    print(f"index: {index}, value: {yearly_salary}")
