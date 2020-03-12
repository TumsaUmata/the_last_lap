class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            dp[0][i] = 1

        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0

        if m == 1 or n == 1:
            return 1

        memo = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                memo[j] = memo[j] + memo[j - 1]
        return memo[-1]


def main():
    s = Solution2()
    print(s.uniquePaths(3, 2))


if __name__ == '__main__':
    main()
