class Solution:
    def isSafe(self, board: list[list[str]], row: int, col: int, n: int) -> bool:
        # horizontal
        for j in range(n):
            if board[row][j] == 'Q':
                return False

        # vertical
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # left diagonal (upper-left)
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # right diagonal (upper-right)
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nQueens(self, board: list[list[str]], row: int, n: int, ans: list[list[str]]) -> None:
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row][j] = 'Q'
                self.nQueens(board, row + 1, n, ans)
                board[row][j] = '.'

    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.nQueens(board, 0, n, ans)
        return ans


sol = Solution()

print(sol.solveNQueens(n = 9))
print(sol.solveNQueens(n = 4))
print(sol.solveNQueens(n = 2))
print(sol.solveNQueens(n = 1))