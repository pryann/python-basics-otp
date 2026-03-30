yearly_salaries = [
    50_000,
    60_000,
    70_000,
    80_000,
    90_000,
    100_000,
    110_000,
    120_000,
]

print("index 0:", yearly_salaries[0])
print("to the 2.:", yearly_salaries[:2])
print("from the 2.:", yearly_salaries[2:])
print("from the 2. to 4.:", yearly_salaries[2:4])
print("from the 2. to 6. with step 2:", yearly_salaries[2:7:2])
print("last element:", yearly_salaries[-1])
print("reversed:", yearly_salaries[::-1])

yearly_salaries_copy = yearly_salaries[:]
