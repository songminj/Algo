# n과 m (8)

n, m = map(int, input().split())
digits = sorted(list(map(int, input().split())))

def perm(start, m, lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    for i in range(start, n):
        perm(i, m, lst+[str(digits[i])])

perm(0, m, [])