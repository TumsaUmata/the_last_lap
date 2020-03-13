def convert_to_frequency(string: str) -> int:
    frequency = 0
    base = string[0]
    for str in string:
        if str < base:
            base = str
            frequency = 1
        elif str == base:
            frequency += 1
    return frequency


def compare_strings(a: str, b: str):
    a = a.split(', ')
    b = b.split(', ')
    frequency_one = [convert_to_frequency(s) for s in a]
    frequency_two = [convert_to_frequency(s) for s in b]
    result = [sum([f1 < f2 for f1 in frequency_one]) for f2 in frequency_two]
    return result


def main():
    string1 = "abcd, aabc, bd"
    string2 = "aaa, aa"

    string3 = "abcd, aabc, bbd"
    string4 = "aaa, aa, aaa"

    print(compare_strings(string1, string2))
    print(compare_strings(string3, string4))


if __name__ == '__main__':
    main()
