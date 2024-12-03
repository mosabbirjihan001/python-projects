def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # Add the first row
        if matrix and matrix[0]:  # Rotate the remaining matrix
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]  # Add the last row in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Spiral order: {spiral_order(matrix)}")
