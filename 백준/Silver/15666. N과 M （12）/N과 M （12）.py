# n과 m (12)

n, m = map(int, input().split())
digits = sorted(list(map(int, input().split())))

def perm(idx, m, lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    before = 0
    for i in range(idx, n):
        if before != digits[i]:
            before = digits[i]
            perm(i, m, lst + [str(digits[i])])

perm(0, m, [])