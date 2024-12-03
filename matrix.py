def find_min_max(matrix):
    flat_matrix = [num for row in matrix for num in row]
    return max(flat_matrix), min(flat_matrix)

rows = int(input("Enter the number of rows: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split())) for i in range(rows)]
maximum, minimum = find_min_max(matrix)
print(f"Maximum: {maximum}, Minimum: {minimum}")
