from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """with sort"""
        frequency_dict = dict()
        for str in strs:
            key = tuple(sorted(str))
            frequency_dict[key] = frequency_dict.get(key, []) + [str]
        return frequency_dict.values()


class Solution2:
    def groupAnagrams(self, strs):
        """without sort"""
        frequency_dict = defaultdict(list)
        for str in strs:
            arr = [0] * 26
            for char in str:
                arr[ord(char) - ord('a')] += 1
            frequency_dict[tuple(arr)].append(str)
        return list(frequency_dict.values())


class Solution3:
    def groupAnagrams(self, strs):
        """best in performance"""
        words_dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in words_dict:
                words_dict[key] = [str]
            else:
                words_dict[key] += [str]
        return list(words_dict.values())


if __name__ == '__main__':
    s = Solution3()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
