from collections import deque

num = int(input())
queue = deque(list(range(1, num+1)))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)