"""Problem reduces to number of connected components in undirected graph"""

from collections import defaultdict, deque


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


class Solution2:
    def makeConnected(self, n, connections):
        number_of_cables = len(connections)

        if number_of_cables < n - 1:
            return -1

        self.graph = defaultdict(list)
        for i, j in connections:
            self.graph[i].append(j)
            self.graph[j].append(i)

        number_of_connected_components = 0
        self.seen = set()
        for node in range(n):
            if node not in self.seen:
                number_of_connected_components += 1
                self.seen.add(node)
                self.dfs(node)
        return number_of_connected_components - 1

    def dfs(self, node):
        """dfs recursive"""
        for neighbor in self.graph[node]:
            if neighbor not in self.seen:
                self.seen.add(neighbor)
                self.dfs(neighbor)


class Solution3:
    def makeConnected(self, n, connections):
        number_of_cables = len(connections)
        if number_of_cables < n - 1:
            return -1

        self.graph = defaultdict(list)
        for i, j in connections:
            self.graph[i].append(j)
            self.graph[j].append(i)

        self.visited = set()
        number_of_connected_cables = 0
        for node in range(n):
            if node not  in self.visited:
                number_of_connected_cables += 1
                self.visited.add(node)
                self.dfs(node)

        return number_of_connected_cables - 1

    def dfs(self, node):
        """dfs iterative"""
        stack = [node]
        while stack:
            next_node = stack.pop()
            for neighbor in self.graph[next_node]:
                if neighbor not in self.visited:
                    stack.append(neighbor)
                    self.visited.add(neighbor)


class Solution4:
    def makeConnected(self, n, connections):
        number_of_cables = len(connections)

        if number_of_cables < n - 1:
            return -1

        self.graph = defaultdict(list)
        for i, j in connections:
            self.graph[i].append(j)
            self.graph[j].append(i)

        number_of_connected_components = 0
        self.visited = set()
        for node in range(n):
            if node not in self.visited:
                number_of_connected_components += 1
                self.visited.add(node)
                self.bfs(node)
        return number_of_connected_components - 1

    def bfs(self, node):
        queue = deque()
        queue.append(node)
        while queue:
            next_node = queue.popleft()
            for neighbor in self.graph[next_node]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.add(neighbor)


def main():
    s = Solution3()
    print(s.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))
    print(s.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
    print(s.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))
    print(s.makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]]))


if __name__ == '__main__':
    main()
