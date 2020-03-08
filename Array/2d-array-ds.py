def hourglassSum(arr):
    max_sum = float('-inf')
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) -2):
            hour_glass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if hour_glass_sum > max_sum:
                max_sum = hour_glass_sum
    return max_sum
