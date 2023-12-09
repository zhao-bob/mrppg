for n in range(100, 1, -1):
    if n%2 == 0:
        continue
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            # 结束内循环
            break
    else:
        print(n)
        # 结束外循环
        break
