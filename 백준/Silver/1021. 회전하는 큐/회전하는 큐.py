import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
queue = deque([i for i in range(1,N+1)])
cnt = 0

for n in nums:
    while True:
        if queue[0] == n: 
            queue.popleft()
            break 
        else: 
            if queue.index(n) <= len(queue)//2:
                queue.rotate(-1)
            else: 
                queue.rotate(1)
            cnt += 1
print(cnt)