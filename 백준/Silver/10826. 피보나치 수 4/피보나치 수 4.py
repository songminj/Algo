N = int(input())
M = {0:0, 1:1}

def fib(n):
    if n in M:
        return M[n]
    elif (n % 2):
        p = (n-1) // 2
        M[p] = fib(p)
        M[p+1] = fib(p+1)
        return fib(p)**2 + fib(p+1)**2
    else:
        p = n // 2
        M[p] = fib(p)
        M[p - 1] = fib(p - 1)
        return fib(p) * (2 * fib(p - 1) + fib(p))
print(fib(N))