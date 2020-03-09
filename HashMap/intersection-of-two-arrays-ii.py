class Solution:
    def intersect(self, nums1, nums2):
        """using hashmap: O(N) Time Complexity and O(N) Space Complexity"""
        nums1_dict = dict()
        nums2_dict = dict()

        for i in nums1:
            if i in nums1_dict:
                nums1_dict[i] += 1
            else:
                nums1_dict[i] = 1

        for i in nums2:
            if i in nums2_dict:
                nums2_dict[i] += 1
            else:
                nums2_dict[i] = 1

        result_list = []
        for i in nums1_dict:
            if i in nums2_dict:
                intersection_frequency = min(nums1_dict[i], nums2_dict[i])
                result_list.extend([i] * intersection_frequency)

        return result_list


class Solution2:
    def intersect(self, nums1, nums2):
        """using two pointer: O(nlogn) Time Complexity and O(N) Space Complexity"""
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        pointer_one = 0
        pointer_two = 0
        result = []
        while pointer_one < len(nums1) and pointer_two < len(nums2):
            if nums1[pointer_one] == nums2[pointer_two]:
                result.append(nums1[pointer_one])
                pointer_one += 1
                pointer_two += 1
            elif nums1[pointer_one] < nums2[pointer_two]:
                pointer_one += 1
            else:
                pointer_two += 1
        return result


class Solution3:
    def intersect(self, nums1, nums2):
        """using binary search: O(m * nlogn) and O(N) Space Complexity"""
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums2 = sorted(nums2)
        result = []
        for num in nums1:
            index = self.binary_search(nums2, num)
            if index != -1:
                result.append(nums2[index])
                nums2.pop(index)
        return result

    def binary_search(self, nums, num):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == num:
                return mid
            if nums[mid] > num:
                right = mid - 1
            elif nums[mid] < num:
                left = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution3()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
