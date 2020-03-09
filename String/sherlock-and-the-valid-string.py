def isValid(s):
    frequency_dict = {}
    for item in s:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    frequency_list = list(frequency_dict.values())
    frequency_set = set(frequency_list)

    if len(frequency_set) == 1:
        return "YES"
    else:
        frequency_dict = {}
        for item in frequency_list:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1

        values = list(frequency_dict.values())
        keys = list(frequency_dict.keys())
        if len(values) == 2:
            if (keys[1] - keys[0] <= 1) and (values[1] == 1):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
