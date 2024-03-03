# n과 m (9)

n, m = map(int, input().split())
digits = sorted(list(map(int, input().split())))

def perm(m, lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    before = 0
    for i in range(n):
        if before != digits[i] and visited[i] == 0:
            before = digits[i]
            visited[i] = 1
            perm(m, lst + [str(digits[i])])
            visited[i] = 0
visited = [0] * n
perm(m, [])
