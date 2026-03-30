matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12, 13],
]

print(matrix[0][0])
print(matrix[2][2])

for row in matrix:
    for element in row:
        print(element)


# 3*3 0,1,2

# V1
# m = [[0, 1, 2]] * 3
# print("V1: ")
# print(m)

m = []
for i in range(3):
    row = []
    for j in range(3):
        # [0, 1, 2]
        row.append(j)
    # m = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    m.append(row)

print("V2: ")
print(m)

# V3
# m = [[j for j in range(3)] for i in range(3)]
# print("V3: ")
# print(m)
