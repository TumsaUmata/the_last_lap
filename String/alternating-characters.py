class Solution:
    def alternatingCharacters(self, s):
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
        return count


class Solution2:
    def alternativeCharacters(self, s):
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
        return count


class Solution3:
    def alternativeCharacters(self, s):
        count = 0
        prev = -1
        for char in s:
            if char == prev:
                count += 1
            prev = char
        return count


if __name__ == '__main__':
    s = Solution()
    s.alternatingCharacters("")
