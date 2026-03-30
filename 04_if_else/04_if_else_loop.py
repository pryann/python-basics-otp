yearly_salaries = [
    50_000,  # 0
    60_000,  # 1
    70_000,  # 2
    80_000,  # 3
    110_000,  # 4
    120_000,  # 5
]
high_salary_threshold = 100_000
sum_low_salaries = 0
sum_high_salaries = 0

for yearly_salary in yearly_salaries:
    if yearly_salary > high_salary_threshold:
        sum_high_salaries += yearly_salary
    else:
        sum_low_salaries += yearly_salary

print("sum low salaries:", sum_low_salaries)
print("sum high salaries:", sum_high_salaries)
