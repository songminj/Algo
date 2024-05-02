N = int(input())
M = {0:0, 1:1}

def f(n):
    if n in M:
        return M[n]
    elif (n % 2):
        k = (n-1) //2
        M[k] = f(k) % 1000000
        M[k+1] = f(k+1) % 1000000
        return f(k)**2 + f(k+1)**2
    else:
        k = n //2
        M[k] = f(k) % 1000000
        M[k-1] = f(k-1) % 1000000
        return f(k)*(2*f(k-1) + f(k))
print(f(N)%1000000)
