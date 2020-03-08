def minimumSwaps(arr):
    n = len(arr)
    number_of_swaps = 0
    for i in range(0, n - 1):
        while arr[i] != i + 1:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            number_of_swaps += 1

    return number_of_swaps
