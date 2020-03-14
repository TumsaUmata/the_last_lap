def maximum_time(T):
    if T[0] == "?":
        if T[1] != "?":
            if int(T[1]) > 3:
                T = "1" + T[1:]
            else:
                T = "2" + T[1:]
        else:
            T = "2" + T[1:]
    if T[1] == "?":
        if T[0] == "2":
            T = T[:1] + "3" + T[2:]
        else:
            T = T[:1] + "9" + T[2:]
    if T[3] == "?":
        T = T[:3] + "5" + T[4:]
    if T[4] == "?":
        T = T[:4] + "9"
    return T


def main():
    time_1 = "??:??"
    print(maximum_time(time_1))


if __name__ == '__main__':
    main()
