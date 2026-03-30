net_prices = [100, 200, 300, 400, 500]
vat_rate = 0.27

gross_prices = []

for i in net_prices:
    gross_prices.append(i * (1 + vat_rate))

print(gross_prices)

gross_prices = [i * (1 + vat_rate) for i in net_prices]

numbers = [1, 2, 3, 4, 5]

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# flatten_matrix = []
# for row in matrix:
#     for element in row:
#         flatten_matrix.append(element)

flatten_matrix = [element for row in matrix for element in row]
print(flatten_matrix)
