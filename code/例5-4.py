def yanghui(t):
    print([1])
    line = [1, 1]
    print(line)
    for i in range(2, t):
        r = []
        for j in range(0, len(line) - 1):
            r.append(line[j] + line[j + 1])
        line = [1] + r + [1]
        print(line)


yanghui(6)
