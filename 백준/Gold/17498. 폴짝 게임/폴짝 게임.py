# 17498번 폴짝게임

import sys
input = sys.stdin.readline

def find(x, y, dp):
    res = -float('inf')
    for i in range(max(0, x-D), x):
        j_start = max(0, y-(D-(x-i)))
        j_end = min(y+(D-(x-i))+1, M)
        for j in range(j_start, j_end):
            tmp = dp[i][j] + arr[i][j]*arr[x][y]
            if tmp > res:
                res = tmp
    return res

def check():
    dp = [[0] * (M) for _ in range(N)]
    for i in range(1, N):
        for j in range(M):
            dp[i][j] = find(i, j, dp)
    return max(dp[-1])

N, M, D = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(N)]
print(check())