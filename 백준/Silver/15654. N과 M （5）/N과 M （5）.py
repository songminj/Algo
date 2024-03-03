# n과 m (5)

# n, m
n, m = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort()

def perm(m, lst):
    if len(lst) == m:
        print(' '.join(lst))
    for i in range(n):
        if str(digits[i]) not in lst:
            perm(m, lst + [str(digits[i])])


perm(m, [])
