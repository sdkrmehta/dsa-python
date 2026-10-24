def exist(board, word):
    m = len(board)
    n = len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def find(i, j, idx):
        if idx == len(word):
            return True

        # Boundary and visited checks
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "$":
            return False

        # Character mismatch check
        if board[i][j] != word[idx]:
            return False

        # Mark as visited
        temp = board[i][j]
        board[i][j] = "$"

        # Explore 4 orthogonal directions
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if find(new_i, new_j, idx + 1):
                return True

        # Backtrack
        board[i][j] = temp
        return False

    # Search for the word starting from any matching cell
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and find(i, j, 0):
                return True

    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))