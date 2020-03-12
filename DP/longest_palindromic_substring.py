class Solution:
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            result = max(result, self.expand(s, i, i), self.expand(s, i, i + 1), key=len)
        return result

    def expand(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


class Solution2:
    def longestPalindrome(self, s):
        dp = [[0] * len(s) for _ in range(len(s))]
        result = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if result == "" or max_length < j - i + 1:
                        result = s[i:j + 1]
                        max_length = j - i + 1
        return result


def main():
    s = Solution2()
    print(s.longestPalindrome("babad"))


if __name__ == '__main__':
    main()
