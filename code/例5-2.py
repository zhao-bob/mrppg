def demo(s):
    result = [0, 0]
    for ch in s:
        if ch.islower():
            result[1] += 1
        elif ch.isupper():
            result[0] += 1
    return tuple(result)

print(demo('Python小屋'))           # 输出：(1, 5)
