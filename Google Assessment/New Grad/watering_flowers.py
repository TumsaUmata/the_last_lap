# class Solution:
#     def waterPlants(self, plants, capacity1, capacity2):
#
#         if len(plants) == 0:
#             return 0
#
#         pointer1 = 0
#         pointer2 = len(plants) - 1
#
#         can1 = capacity1
#         can2 = capacity2
#         count = 2
#
#         while pointer1 != pointer2:
#             if can1 >= plants[pointer1]:
#                 can1 -= plants[pointer1]
#                 pointer1 += 1
#             else:
#                 can1 = capacity1
#                 can1 -= plants[pointer1]
#                 pointer1 += 1
#                 count += 1
#
#             if can2 >= plants[pointer2]:
#                 can2 -= plants[pointer2]
#                 pointer2 -= 1
#             else:
#                 can2 = capacity2
#                 can2 -= plants[pointer2]
#                 pointer2 -= 1
#                 count += 1
#
#             if (pointer1 == pointer2):
#                 if ((can1 + can2) >= plants[pointer1]):
#                     return count
#                 else:
#                     return count + 1
#
#             elif pointer2 < pointer1:
#                 return count
#
#
# if __name__ == "__main__":
#     arr = [2, 4, 5, 1, 2]
#     c1 = 5
#     c2 = 7
#     print(Solution().waterPlants(arr, c1, c2))


import math


def solution(plants, cap1, cap2):
    if len(plants) == 0: return 0
    end_m = len(plants) // 2
    if (len(plants) % 2 == 0):
        start_f = len(plants) / 2
    else:
        start_f = len(plants) // 2 + 1
    water_needed_m = sum(plants[:end_m])
    water_needed_f = sum(plants[start_f:])
    refill_m = math.ceil(water_needed_m / cap1)
    refill_f = math.ceil(water_needed_f / cap2)
    if (len(plants) % 2 != 0):
        total_water_needed = water_needed_m + water_needed_f + plants[end_m]
        total_water_filled = cap1 * refill_m + cap2 * refill_f
        if (total_water_needed > total_water_filled):
            refill_m += 1
    return refill_m + refill_f


print(solution([2, 4, 5, 1, 2], 5, 7))
