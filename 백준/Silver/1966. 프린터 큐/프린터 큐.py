from collections import deque

tc = int(input())

for _ in range(tc):
    # n : 문서의 개수, m :몇번째로 인쇄되는지 궁금한 문서의 queue의 위치
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    target = queue[m]
    queue[m] = 0
    done = []
    while len(queue) > 0:
        if queue[0] == 0:
            if max(queue) > target:
                queue.rotate(-1)
            else:
                printed = queue.popleft()
                done += [printed]
        else:
            if queue[0] == max(queue):
                if queue[0] < target:
                    queue.rotate(-1)
                else:
                    printed = queue.popleft()
                    done += [printed]
            else:
                queue.rotate(-1)
        if 0 in done:
            break

    print(len(done))