# 13335번 트럭

import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().strip().split())
trucks = deque(list(map(int, input().strip().split())))
bridge = deque([0] * w)
time = 0

while bridge:
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

print(time)