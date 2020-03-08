def number_needed(a, b):
    chars_dict = dict()

    for char in a:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    for char in b:
        if char in chars_dict:
            chars_dict[char] -= 1
        else:
            chars_dict[char] = -1

    sum_diff = 0
    for char in chars_dict.keys():
        sum_diff += abs(chars_dict[char])

    return sum_diff
