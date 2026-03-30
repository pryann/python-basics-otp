# IMMUTABLE

age = 33
age_copy = age

print(age, id(age))
print(age_copy, id(age_copy))

# 0x0001 (33) <---- age
#             ^---- age_copy

age = 30
print(age, id(age))
print(age_copy, id(age_copy))

# 0x0001 (33) <---- age_copy
# 0x0002 (30) <---- age


# MUTABLE
yearly_salaries = [50_000, 55_000, 60_000]
yearly_salaries_copy = yearly_salaries

print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

yearly_salaries.append(100_000)
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

yearly_salaries_copy.remove(55_000)
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

# assignment operator
yearly_salaries = [10_100, 20_000]
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

# COPY
yearly_salaries_copy = yearly_salaries.copy()
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
