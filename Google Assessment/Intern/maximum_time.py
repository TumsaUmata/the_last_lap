def maximum_time(time):
    if time[0] == "?":
        if time[1] != "?":
            if int(time[1]) > 3:
                time = "1" + time[1:]
            else:
                time = "2" + time[1:]
        else:
            time = "2" + time[1:]
    if time[1] == "?":
        if time[0] == "2":
            time = time[:1] + "3" + time[2:]
        else:
            time = time[:1] + "9" + time[2:]
    if time[3] == "?":
        time = time[:3] + "5" + time[4:]
    if time[4] == "?":
        time = time[:4] + "9"
    return time


def main():
    time_1 = "??:??"
    print(maximum_time(time_1))


if __name__ == '__main__':
    main()
