# Create a 3x3 matrix filled with zeros
matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Fill the matrix with values (example: row * col)
for i in range(4):
    for j in range(4):
        matrix[i][j] = 1  # Just an example pattern

# Print the matrix
for x in matrix:
    print(x)