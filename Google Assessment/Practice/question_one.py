def solution(A):
    max_value = float('-inf')
    rows_created = 0
    for i in A:
        if i > max_value:
            rows_created += 1
            max_value = i
    return rows_created


def main():
    print(solution([5, 4, 3, 6, 1, 7, 6]))


if __name__ == '__main__':
    main()
