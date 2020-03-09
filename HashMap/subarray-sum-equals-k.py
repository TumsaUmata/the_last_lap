class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sums = 0
        nums_dict = dict()
        nums_dict[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += nums_dict.get(sums - k, 0)
            nums_dict[sums] = nums_dict.get(sums, 0) + 1
        return count
