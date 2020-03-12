"""Problem reduces to number of connected components in undirected graph"""


class Solution:
    def __init__(self):
        self.visited = [0]

    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1
        graph = [set() for _ in range(n)]
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)

        self.visited *= n

        return sum(self.dfs(graph, i, self.visited) for i in range(n)) - 1

    def dfs(self, graph, first, visited):
        """dfs recursively"""
        if visited[first]:
            return 0
        visited[first] = 1
        for second in graph[first]:
            self.dfs(graph, second, visited)
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))
