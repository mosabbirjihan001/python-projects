def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        if col >= n:
            result.append(["".join("Q" if c == 1 else "." for c in row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    result = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return result

n = 4
solutions = solve_n_queens(n)
for sol in solutions:
    print("\n".join(sol), "\n")
