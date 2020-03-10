if __name__ == '__main__':
    numbers = [6, 5, 3, 7, 2, 4, 1]

    numbers = sorted(numbers)
    print(numbers)

    numbers = sorted(numbers, reverse=True)
    print(numbers)

    numbers = list(reversed(sorted(numbers)))
    print(numbers)

    animals = [
        {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
        {'type': 'elephant', 'name': 'Devon', 'age': 3},
        {'type': 'puma', 'name': 'Moe', 'age': 5},
    ]

    animals = sorted(animals, key=lambda animal: animal['age'])
    print(animals)
