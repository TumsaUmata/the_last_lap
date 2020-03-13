def largest_subarray(a, k):
    first_index = 0
    for index in range(1, len(a) - k + 1):
        if a[first_index] < a[index]:
            first_index = index

    return a[first_index:first_index + k]


def main():
    a = [1, 9, 2, 7, 9, 3]
    print(largest_subarray(a, 2))


if __name__ == '__main__':
    main()
