import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    campus = {}
    for _ in range(N):
        S, L = input().split()
        campus[S] = campus.get(S, 0) + int(L)
    ans = sorted(list(campus.items()), key=lambda x:x[1], reverse=True)
    print(ans[0][0])