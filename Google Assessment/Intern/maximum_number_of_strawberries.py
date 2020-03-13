def strawberry(num, n, arr):
    dp = [[False] * (num+1) for i in range(n+1)]
    dp[0][0] = True
    res = 0
    for i in range(1, n+1):
        dp[i][0] = True
        dp[i][arr[i-1]] = True
        for j in range(1, num+1):
            if j - arr[i-1] >= 0 and i > 1:
                dp[i][j] = dp[i-2][j-arr[i-1]]
            dp[i][j] = dp[i][j] or dp[i-1][j]
            if dp[i][j]:
                res = max(res, j)
    return res


def strawberry1(num, n, arr):
    dp = [[0] * (num + 1) for _ in range(len(arr) + 1)]
    for i in range(arr[0], num + 1):
        dp[1][i] = arr[0]
    for i in range(2, len(arr) + 1):
        for j in range(1, num + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= arr[i - 1]:
                dp[i][j] = max(dp[i][j],
                               dp[i - 2][j - arr[i - 1]] + arr[i - 1])  # here is the only thing that changed: "i - 2"
    return dp[-1][-1]


print(strawberry1(100, 5, [50, 10, 20, 30, 40])) # 90
