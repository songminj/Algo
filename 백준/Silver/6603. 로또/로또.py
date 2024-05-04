import sys
input = sys.stdin.readline


def perm(lst, p):
    if len(lst) == 6:
        print(*lst)
        return
    for i in range(p, k):
        perm(lst+[S[i]], i+1)

while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    visited = [False] * (k+1)
    perm([], 0)
    print()