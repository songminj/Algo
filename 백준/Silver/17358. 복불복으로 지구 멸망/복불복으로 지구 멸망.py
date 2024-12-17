# 17358번 복불복으로 지구 멸망

import sys
input = sys.stdin.readline

N = int(input()) -1

ans = 1
for i in range(N, 1, -2):
    ans = ans * i
print(ans % ( 10**9 + 7))