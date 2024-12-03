def word_search(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(x, y, index):
        if index == len(word):
            return True
        if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != word[index]:
            return False
        temp, board[x][y] = board[x][y], '#'
        found = (dfs(x + 1, y, index + 1) or
                 dfs(x - 1, y, index + 1) or
                 dfs(x, y + 1, index + 1) or
                 dfs(x, y - 1, index + 1))
        board[x][y] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "hello"
print(f"Word exists: {word_search(board, word)}")
