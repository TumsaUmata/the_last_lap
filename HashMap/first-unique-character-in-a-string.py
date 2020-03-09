class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars_dict = dict()
        for i in s:
            if i in chars_dict:
                chars_dict[i] += 1
            else:
                chars_dict[i] = 1

        candidates = set()
        for i in chars_dict:
            if chars_dict[i] == 1:
                candidates.add(i)

        for i in range(len(s)):
            if s[i] in candidates:
                return i

        return -1


class Solution2:
    def firstUniqChar(self, s):
        chars_dict = {}
        for char in s:
            if char in chars_dict.keys():
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1

        for i in range(len(s)):
            char = s[i]
            if chars_dict[char] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = Solution2()
    print(s.firstUniqChar("loveleetcode"))
