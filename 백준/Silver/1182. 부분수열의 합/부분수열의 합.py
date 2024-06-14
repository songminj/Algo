# 1182번 부분수열의 합

n, s = map(int, input().strip().split())
arr = sorted(list(map(int, input().strip().split())))
res = 0
def dfs(cnt, k):
    global res
    if k == n:
        if cnt == s:
            res += 1
        return
    dfs(cnt+arr[k], k+1)
    dfs(cnt, k+1)

dfs(0, 0)
if s == 0:
    print(res-1)
else:
    print(res)