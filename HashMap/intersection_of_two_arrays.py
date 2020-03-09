class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)

        return result
