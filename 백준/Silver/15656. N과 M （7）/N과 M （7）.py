import sys

input = sys.stdin.readline

n, m = map(int, input().split())
digits = sorted(list(map(int, input().split())))

def perm(idx, res):
    if idx == m:
        print(' '.join(res))
        return
    for i in range(n):
        res.append(str(digits[i]))
        perm(idx+1, res)
        res.pop()

perm(0, [])