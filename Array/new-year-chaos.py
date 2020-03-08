def minimumBribes(q):
    count = 0
    for i in range(len(q) - 1, 0, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                count += 1
                q[i], q[i - 1] = q[i - 1], q[i]
            elif q[i - 2] == i + 1:
                count += 2
                q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
                q[i - 1], q[i] = q[i], q[i - 1]
            else:
                return "Too chaotic"
    print(count)
