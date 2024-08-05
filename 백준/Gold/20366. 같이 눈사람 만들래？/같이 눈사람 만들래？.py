# 20366번 같이 눈사람 만들래?
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
res = int(4e9) +1
arr.sort()

for i in range(n-3):
    for j in range(i+3, n):
        l, r = i+1, j-1
        snow1 = arr[i]+arr[j]
        while l < r:
            tmp = snow1-arr[l]-arr[r]
            if abs(tmp) < res:
                res = abs(tmp)
            if tmp < 0:
                r -= 1
            else:
                l += 1
print(res)