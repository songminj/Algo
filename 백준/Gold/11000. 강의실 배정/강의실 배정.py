import sys
from heapq import heappush, heappop

# input 받기
n = int(sys.stdin.readline())
time = []
visited = [False] * n
for _ in range(n):
    t = list(map(int, sys.stdin.readline().strip().split()))
    time.append(t)
time.sort()

# time을 정렬한 후 최소로 강의실을 이용하는 case를 res++ 해줌
room = []
heappush(room, time[0][1])
for i in range(1, n):
    if time[i][0] < room[0]:
        heappush(room, time[i][1])
    else:
        heappop(room)
        heappush(room, time[i][1])
print(len(room))