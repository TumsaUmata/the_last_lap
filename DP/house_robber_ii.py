class Solution:
    def rob(self, nums) -> int:
        nums_length = len(nums)
        if not nums:
            return 0
        if nums_length == 1:
            return nums[0]
        if nums_length == 2:
            return max(nums)

        first_nums = nums[1::]
        second_nums = nums[:0-1]
        return max(self.rob_easily(first_nums), self.rob_easily(second_nums))

    def rob_easily(self, nums) -> int:
        nums = [0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        return nums[-1]


def main():
    s = Solution()
    print(s.rob([1, 2, 3, 1]))


if __name__ == '__main__':
    main()
