def f2(n, i):
    cache2 = dict()
    
    def f(n, i):
        if n==i or i==0:
            return 1
        elif (n,i) not in cache2:
            cache2[(n,i)] = f(n-1, i) + f(n-1, i-1)
        return cache2[(n,i)]
    
    return f(n,i)

print(f2(60,9))
