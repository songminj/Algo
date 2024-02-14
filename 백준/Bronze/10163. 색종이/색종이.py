import sys

# 색종이 장수
num = int(input())
arr = list([0]*(1001) for _ in range(1001))
# area = {}
for i in range(1, num+1):
    x1, y1, w, h = map(int, sys.stdin.readline().strip().split())
    # area[i] = loc + [abs((loc[2]+loc[0]) * loc[3]-loc[1])]
    for p in range(w):
        for q in range(h):
            arr[x1+p][y1+q] = i


for target in range(1, num+1):
    cnt = 0
    for i in range(1001):
        cnt += arr[i].count(target)
    print(cnt)

