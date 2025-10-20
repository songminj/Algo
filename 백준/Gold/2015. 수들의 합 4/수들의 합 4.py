# 2015번 수들의 합 4

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
sum_dict = {0 : 1}
sum_val = 0
ans = 0

for i in arr:
    sum_val += i
    if sum_val - K in sum_dict.keys():
        ans += sum_dict[sum_val-K]
    sum_dict[sum_val] = sum_dict.get(sum_val, 0) + 1

print(ans)