def demo(n):
    def isPrime(p):
        if p == 2:
            return True
        if p%2 == 0:
            return False
        for i in range(3, int(p**0.5)+1, 2):
            if p%i == 0:
                return False
        return True
    
    if isinstance(n, int) and n>0 and n%2==0:
        for i in range(2, n//2+1):
            if isPrime(i) and isPrime(n-i):
                print(i, '+', n-i, '=', n)

demo(66)
