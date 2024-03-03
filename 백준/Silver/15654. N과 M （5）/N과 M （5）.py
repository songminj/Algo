# n과 m (5)

# n, m
n, m = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort()

def perm(m, lst, visited):
    if len(lst) == m:
        print(' '.join(lst))
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            perm(m, lst + [str(digits[i])], visited)
            visited[i] = 0

visited = [0] * n
perm(m, [], visited)
