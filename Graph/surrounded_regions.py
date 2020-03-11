from collections import deque


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


class Solution2:
    def solve(self, board):
        if not board:
            return

        queue = deque()
        rows = len(board)
        columns = len(board[0])

        for row in range(rows):
            for col in range(columns):
                if (row == 0 or col == 0 or row == rows - 1 or col == columns - 1) and board[row][col] == "O":
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            board[row][col] = "T"
            for x_axis, y_axis in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_row = row + x_axis
                new_col = col + y_axis
                if 0 <= new_row < rows and 0 <= new_col < columns and board[new_row][new_col] == "O":
                    queue.append((new_row, new_col))

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
