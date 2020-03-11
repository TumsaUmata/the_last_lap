from collections import deque


class Solution:

    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        number_of_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    self.bfs(grid, row, col)
                    number_of_islands += 1

        return number_of_islands

    def bfs(self, grid, row, col):
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue.append((row, col))
        while queue:
            (x_axis, y_axis) = queue.popleft()
            for direction in directions:
                new_row = x_axis + direction[0]
                new_col = y_axis + direction[1]
                if self.check_validity(grid, new_row, new_col) \
                        and grid[new_row][new_col] == '1':
                    grid[new_row][new_col] = '0'
                    queue.append((new_row, new_col))

    def check_validity(self, grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    ))
