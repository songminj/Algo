# n과 m (6)

n, m = map(int, input().split())
digits = sorted(list(map(int, input().split())))

def perm(start, lst):
    if len(lst) == m:
        print(' '.join(lst))
    for i in range(start, n):
        perm(i+1, lst + [str(digits[i])])

perm(0, [])