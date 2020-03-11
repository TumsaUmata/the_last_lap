from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        row_length = len(grid)
        column_length = len(grid[0])
        visited = [[0] * column_length for _ in range(row_length)]

        max_area = 0
        for i in range(row_length):
            for j in range(column_length):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    max_area = max(max_area, self.bfs(grid, visited, i, j))
        return max_area

    def bfs(self, grid, visited, row, col):
        row_length = len(grid)
        column_length = len(grid[0])

        queue = deque()
        queue.append((row, col))
        visited[row][col] = 1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        area = 1
        while queue:
            row, col = queue.popleft()
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < row_length and 0 <= new_col < column_length and \
                        visited[new_row][new_col] == 0 and grid[new_row][new_col] == 1:
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = 1
                    area += 1
        return area


if __name__ == '__main__':
    board = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]

    s = Solution()
    print(s.maxAreaOfIsland(board))
