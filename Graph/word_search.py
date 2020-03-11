class Solution:
    def exist(self, grid, word: str) -> bool:
        if not grid:
            return False

        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if self.dfs(grid, i, j, word):
                    return True
        return False

    def dfs(self, grid, row, col, word):
        if not word:
            return True

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or word[0] != grid[row][col]:
            return False

        temp = grid[row][col]
        grid[row][col] = "1"

        result = self.dfs(grid, row + 1, col, word[1:]) or self.dfs(grid, row - 1, col, word[1:]) \
                 or self.dfs(grid, row, col + 1, word[1:]) or self.dfs(grid, row, col - 1, word[1:])
        grid[row][col] = temp
        return result


if __name__ == '__main__':
    s = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    print(s.exist(board, "ABCCED"))
    print(s.exist(board, "SEE"))
    print(s.exist(board, "ABCB"))
