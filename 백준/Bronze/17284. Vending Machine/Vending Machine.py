# 17248번 Vending Machine

import sys
input = sys.stdin.readline

btn = list(map(int, input().strip().split()))
n= len(btn)
order = [0, 0, 0, 0]
for i in btn:
    order[i] += 1

res = 5000 - order[1] * 500 - order[2] * 800 - order[3] *1000
print(res)