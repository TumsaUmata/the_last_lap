class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        nums_length = len(nums)

        cache = [1 for _ in range(nums_length)]

        for i in range(nums_length):
            for j in range(i):
                if nums[i] > nums[j]:
                    cache[i] = max(cache[i], cache[j] + 1)
        return max(cache)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
