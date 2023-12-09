from random import randint

def mul(a, b):
    aa = list(map(int, reversed(str(a))))
    bb = list(map(int, reversed(str(b))))
    result = [0] * (len(aa)+len(bb))
    for ia, va in enumerate(aa):
        c = 0
        for ib, vb in enumerate(bb):
            c, result[ia+ib] = divmod(va*vb+c+result[ia+ib], 10)
        result[ia+ib+1] = c

    result = int(''.join(map(str,reversed(result))))
    return result

for i in range(100000):
    a = randint(1, 1000)
    b = randint(1, 1000)
    r = mul(a, b)
    if r != a*b:
        print(a, b, r, 'error')
