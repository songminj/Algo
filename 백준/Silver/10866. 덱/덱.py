import sys
from collections import deque
deq = deque([])
order = int(sys.stdin.readline())

for _ in range(order):
    new = sys.stdin.readline().split()
    if new[0] == 'push_front':
        deq.appendleft(new[1])
        continue
    elif new[0] == 'push_back':
        deq.append(new[1])
        continue
    elif new[0] == 'pop_front':
        if deq:
            num = deq.popleft()
            print(num)
            continue
        else:
            print(-1)
            continue
    elif new[0] == 'pop_back':
        if deq:
            num = deq.pop()
            print(num)
            continue
        else:
            print(-1)
            continue
    elif new[0] == 'size':
        print(len(deq))
        continue
    elif new[0] == 'empty':
        if deq:
            print(0)
            continue
        else:
            print(1)
            continue
    elif new[0] == 'front':
        if deq:
            print(deq[0])
            continue
        else:
            print(-1)
            continue
    elif new[0] == 'back':
        if deq:
            print(deq[-1])
            continue
        else:
            print(-1)
            continue