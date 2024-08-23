# 19637번 IF문 좀 대신 써줘

import sys

# 이분탐색
def binary_search(k):
    l, r = 0, N-1
    res = 0
    while l <= r:
        mid = (l+r) // 2
        if name_max[mid] >= k:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return name[res]

input = sys.stdin.readline
N, M = map(int, input().strip().split())
name = []
name_max = []
for _ in range(N):
    name_, name_max_ = input().strip().split()
    name.append(name_)
    name_max.append(int(name_max_))
name_max.sort()
# print(name_max)

for _ in range(M):
    k = int(input())
    print(binary_search(k))