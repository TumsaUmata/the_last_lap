class ListComprehension:

    def square(self, number):
        return number * number


if __name__ == '__main__':
    s = ListComprehension()

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = [s.square(number) for number in numbers]
    print(numbers)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = [s.square(number) for number in numbers if number % 2 == 0]
    print(numbers)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = [s.square(number) for number in numbers if number % 2 != 0]
    print(numbers)
