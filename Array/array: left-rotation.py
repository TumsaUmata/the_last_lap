def rotLeft(a, d):
    for i in range(d):
        first = a[0]
        a.remove(first)
        a.append(first)
    return a
