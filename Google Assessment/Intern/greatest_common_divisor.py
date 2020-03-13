# def Solution():
#     n = int(input())
#
#     max_gcd = float('-inf')
#     min_gcd = float('inf')
#
#     for i in range(0, n + 1):
#         if i == 0:
#             input()
#         else:
#             for j in range(0, 2 ** i, 2):
#                 a = input()
#                 b = input()
#                 if a == -1 or b == -1:
#                     continue
#
#                 new_gcd = gcd(a, b)
#                 if new_gcd < min_gcd:
#                     min_gcd = new_gcd
#                 if new_gcd > max_gcd:
#                     max_gcd = new_gcd
#
#     if min_gcd == float('inf') and max_gcd == float('-inf'):
#         print(0)
#         return
#
#     print(max_gcd - min_gcd)
#
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# Solution()
#
#
# """
#
# It said:
# Failed level 3 test case
# Input:
# 3
# 10
# 9 18
# 13 -1 8 8
# 12 26 -1 -1 6 9
# Expected output:
# 7
# Your output:
#
# """


class Solution:
    def maxDiffGCD(self, n, tree):
        if n == -1:
            return -1
        if n == 0:
            return 0

        def findGCD(num1, num2):
            if num2 == 0:
                return num1
            else:
                return findGCD(num2, num1 % num2)

        gcds = []
        for i in range(1, n):
            layer = tree[i]
            for j in range(0, i * 2, 2):
                num1 = max(layer[j], layer[j + 1])
                num2 = min(layer[j], layer[j + 1])
                if num1 == -1 or num2 == -1:
                    continue
                else:
                    gcd = findGCD(num1, num2)
                if not gcds:
                    gcds.append(gcd)
                elif gcd < gcds[0]:
                    gcds = [gcd] + gcds
                elif gcd > gcds[-1]:
                    gcds.append(gcd)
                else:
                    gcds = gcds[:-1] + [gcd] + gcds[-1]
        return gcds[-1] - gcds[0]


def main():
    s = Solution()
    s.maxDiffGCD()


if __name__ == '__main__':
    main()
