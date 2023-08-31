matrix = [[5, 10, 20, 30], [2, 4, 6, 8], [10, 25, 50, 2], [60, 75, 80, 4]]

print("3x3 matrix:\n")
print(matrix)
print("___"*50)
print("row 0, column 0", matrix[0][0])
print("row 0, column 1", matrix[0][1])
print("row 0, column 2", matrix[0][2])
print("row 1, column 0", matrix[1][0])
print("row 1, column 1", matrix[1][1])
print("row 1, column 2", matrix[1][2])
print("row 2, column 0", matrix[2][0])
print("row 2, column 1", matrix[2][1])
print("row 2, column 2", matrix[2][2])

for i in range(0, 3):
    for j in range(0, 3):
        print("row ", i, "column", j, "=", matrix[i][j])

for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end='')
    print()
