M, N = map(int, input().split())
find = [False, False] + [True]*(N-1)

for i in range(2, N+1):
    if find[i]:
        if i >= M:
            print(i)
        for j in range(2*i, N+1, i):
            find[j] = False