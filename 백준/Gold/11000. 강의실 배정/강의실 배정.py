import sys
from heapq import heappush, heappop

# input 받기
n = int(sys.stdin.readline())
time = []
visited = [False] * n
for _ in range(n):
    t = tuple(map(int, sys.stdin.readline().strip().split()))
    time.append(t)
time.sort()

# 시작시간 < 이용중인 회의실의 끝나는시간 이면 새로운 회의실을 열어주고 
room = []
heappush(room, time[0][1])
for i in range(1, n):
    if time[i][0] < room[0]:
        heappush(room, time[i][1])
    # 시작시간 > 이용중인 회의실이 끝나는시간 (= 지금 비어있는 회의실이 있으면) 이면
    # 이용했던 회의실 시간을 빼주고 새로운 회의의 끝나는 시간을 넣어준다. 
    else:
        heappop(room)
        heappush(room, time[i][1])
print(len(room))