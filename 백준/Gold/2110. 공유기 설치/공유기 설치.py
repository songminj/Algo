# 2110번 공유기 설치

import sys
input = sys.stdin.readline

n, c = map(int, input().strip().split())
house = [int(input()) for _ in range(n)]
house.sort()
ans = 0
l, r = 1, house[-1] - house[0]

def check(m):
    cnt = 1
    now = house[0]
    for i in range(1, n):
        if house[i] - now >= m:
            cnt += 1
            now = house[i]
            if cnt == c:
                return True
    return False

while l <= r:
    mid = (l+r) // 2
    if check(mid) :
        ans = mid
        l = mid +1
    else:
        r = mid -1
print(ans)