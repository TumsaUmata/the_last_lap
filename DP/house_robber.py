class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        nums_length = len(nums)
        if nums_length == 1:
            return nums[0]
        if nums_length == 2:
            return max(nums)

        nums[1] = max(nums[0], nums[1])
        for i in range(2, nums_length):
            nums[i] = max(nums[i], nums[i] + nums[i-2], nums[i-1])
        return nums[-1]


class Solution2:
    def rob(self, nums) -> int:
        nums = [0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        return nums[-1]


def main():
    s = Solution2()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 1, 1, 2]))


if __name__ == '__main__':
    main()
