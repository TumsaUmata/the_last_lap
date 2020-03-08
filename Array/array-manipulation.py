def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]

    max_value = 0
    value = 0
    print(arr)
    for i in arr:
        value += i
        if value > max_value:
            max_value = value
    return max_value
