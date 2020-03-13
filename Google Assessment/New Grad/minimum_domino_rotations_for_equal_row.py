from collections import defaultdict


class Solution:
    def minDominoRatations(self, A, B) -> int:
        count_a = defaultdict(int)
        count_b = defaultdict(int)
        N = len(A)
        same = 0

        for i in range(N):
            count_a[A[i]] += 1
            count_b[B[i]] += 1

            if A[i] == B[i]:
                same += 1

        for x in range(1, 7):
            if (count_a[x] + count_b[x] - same) == N:
                return N - max(count_a[x], count_b[x])

        return -1


def main():
    s = Solution()

    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    print(s.minDominoRatations(A, B))


if __name__ == '__main__':
    main()
