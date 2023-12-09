def cni2(n, i):
    if not (isinstance(n,int) and isinstance(i,int) and n>=i):
        print('n and i must be integers and n must be larger than or equal to i.')
        return
    result = 1
    Min, Max = sorted((i,n-i))
    for i in range(n, 0, -1):
        if i > Max:
            result = result * i
        elif i <= Min:
            result = result // i
    return result

print(cni2(6,2))
