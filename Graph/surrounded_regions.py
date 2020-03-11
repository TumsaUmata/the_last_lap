class Solution:
    def solve(self, board) -> None:
        if not board:
            return
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i == 0 or i == (len(board) - 1) or j == 0 or j == (
                        len(board[i]) - 1)):
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] == 'X':
            return
        if board[row][col] == 'T':
            return
        board[row][col] = 'T'
        self.dfs(board, row - 1, col)
        self.dfs(board, row + 1, col)
        self.dfs(board, row, col - 1)
        self.dfs(board, row, col + 1)
