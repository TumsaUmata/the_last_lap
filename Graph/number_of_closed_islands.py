from collections import deque


class Solution:
    def closedIsland(self, grid) -> int:
        number_of_closed_islands = 0

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    if self.isClosedIsland(i, j, grid):
                        number_of_closed_islands += 1

        return number_of_closed_islands

    def isClosedIsland(self, row, col, grid):
        if row - 1 < 0 or col - 1 < 0 or row + 1 >= len(grid) or col + 1 >= len(grid[0]):
            return False

        grid[row][col] = 1
        top = True if grid[row - 1][col] else self.isClosedIsland(row - 1, col, grid)
        bottom = True if grid[row + 1][col] else self.isClosedIsland(row + 1, col, grid)
        left = True if grid[row][col - 1] else self.isClosedIsland(row, col - 1, grid)
        right = True if grid[row][col + 1] else self.isClosedIsland(row, col + 1, grid)

        return top and bottom and left and right


class Solution2:
    def closedIsland(self, grid):
        islands = self.findIslands(grid)
        number_of_closed_islands = 0
        for island in islands:
            if self.isClosed(grid, island):
                number_of_closed_islands += 1
        return number_of_closed_islands

    def findIslands(self, grid):
        islands = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    island = self.bfs(grid, row, col)
                    islands.append(island)
        return islands

    def bfs(self, grid, row, col):
        queue = deque()
        queue.append((row, col))
        island = [(row, col)]
        grid[row][col] = 1
        while queue:
            row, col = queue.popleft()
            for r, c in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                new_row = row + r
                new_col = col + c
                if self.isValid(grid, new_row, new_col):
                    island.append((new_row, new_col))
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 1
        return island

    def isValid(self, grid, row, col) -> bool:
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0:
            return True
        return False

    def isClosed(self, grid, island) -> bool:
        if not island:
            return False
        for row, col in island:
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]
        ]
    ))
