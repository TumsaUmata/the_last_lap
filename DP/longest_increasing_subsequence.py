""""https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step"""
"""https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation"""

class Solution:
    def lengthOfLIS(self, nums) -> int:
        """O(N^2)"""
        if not nums:
            return 0

        nums_length = len(nums)

        cache = [1 for _ in range(nums_length)]

        for i in range(nums_length):
            for j in range(i):
                if nums[i] > nums[j]:
                    cache[i] = max(cache[i], cache[j] + 1)
        return max(cache)


class Solution2:
    def lengthOfLIS(self, nums) -> int:
        """O(NlogN)"""
        subsequence = []
        for num in nums:
            position = self.binary_search(subsequence, num)
            if position == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[position] = num
        return len(subsequence)

    def binary_search(self, subsequence, value: int) -> int:
        left = 0
        right = len(subsequence) - 1
        while left <= right:
            mid = (left + right) // 2
            if subsequence[mid] < value:
                left = mid + 1
            elif subsequence[mid] > value:
                right = mid - 1
            else:
                return mid
        return left


if __name__ == '__main__':
    s = Solution2()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
