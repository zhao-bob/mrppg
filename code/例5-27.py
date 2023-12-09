def primes(maxNumber):
    lst = list(range(3, maxNumber, 2))
    m = int(maxNumber**0.5)
    for index in range(m):
        current = lst[index]
        if current > m:
            break
        lst[index+1:] = filter(lambda x: x%current!=0, lst[index+1:])
    return [2] + lst

print(primes(1000))
