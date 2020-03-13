def convert_to_frequency(string: str) -> int:
    freq = 0
    base = string[0]
    for s in string:
        if s < base:
            base = s
            freq = 1

        elif s == base:
            freq += 1

    return freq


def compare_strings(a: str, b: str):
    s1 = a.split(', ')
    s2 = b.split(', ')
    freq1 = [convert_to_frequency(s) for s in s1]
    freq2 = [convert_to_frequency(s) for s in s2]
    rt = [sum([f1 < f2 for f1 in freq1]) for f2 in freq2]
    return rt


def main():
    string1 = "abcd, aabc, bd"
    string2 = "aaa, aa"

    string3 = "abcd, aabc, bbd"
    string4 = "aaa, aa, aaa"

    print(compare_strings(string1, string2))
    print(compare_strings(string3, string4))


if __name__ == '__main__':
    main()
