# n과 m (10)

n, m = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort()

def perm(idx, m, lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    before = 0
    for i in range(idx, n):
        if before != digits[i]:
            before = digits[i]
            # visited[i] = True
            perm(i+1, m, lst + [str(digits[i])])
            # visited[i] = False
# visited = [False] * n
perm(0, m, [])
