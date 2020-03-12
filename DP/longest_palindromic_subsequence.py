class Solution:
    def longestPalindromicSubseq(self, s: str) -> int:
        len_s = len(s)

        if not s:
            return 0

        if s == s[::-1]:
            return len(s)

        dp = [[0] * len_s for _ in range(len_s)]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(1, len_s):
            for j in range(len_s - i):
                if s[j] == s[j + i]:
                    dp[j][j + i] = 2 + dp[j + 1][j + i - 1]
                else:
                    dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
        return dp[0][-1]


def main():
    s = Solution()
    print(s.longestPalindromicSubseq("bbbab"))


if __name__ == '__main__':
    main()
