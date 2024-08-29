# 5555번 반지

import sys
input = sys.stdin.readline

string = input().strip()
n = int(input())
k = len(string)
cnt = 0
for _ in range(n):
    tg = input().strip()
    tg += tg[:k-1]
    if string in tg:
        cnt += 1
print(cnt)