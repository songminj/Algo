# 1138번 한 줄로 서기

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))
res = [0] * N

for i in range(N):
    cnt = 0
    # 작은 친구들부터 빈자리갯수를 세면서 자리배치
    for j in range(N):
        if res[j] == 0:
            cnt += 1
        if cnt == arr[i]+1:
            res[j] = i+1
            break

print(*res)