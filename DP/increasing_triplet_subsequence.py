class Solution:
    def increasingTriplet(self, nums) -> bool:
        doublet = [float('inf'), float('inf')]
        for num in nums:
            if num <= doublet[0]:
                doublet[0] = num
            elif num <= doublet[1]:
                doublet[1] = num
            else:
                return True
        return False

