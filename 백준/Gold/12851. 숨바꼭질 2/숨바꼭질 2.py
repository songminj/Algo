# 12851번 숨바꼭질2

from collections import deque

n, k = map(int, input().strip().split())

# 방문한 위치를 기록하는 배열 (최소 횟수로만 방문하게)
visited = [-1] * 100001

# BFS 큐 초기화
queue = deque()
queue.append((n, 0))  # (현재 위치, 현재까지의 이동 횟수)
visited[n] = 0  # 시작점은 0번 이동

# 최소 이동 횟수와 해당 횟수로 k에 도달한 경로 수
min_step = float('inf')
cnt = 0

while queue:
    now, step = queue.popleft()

    if now == k:
        if step < min_step:
            min_step = step
            cnt = 1
        elif step == min_step:
            cnt += 1
        continue

    # 현재 위치에서 이동할 수 있는 세 가지 경우
    for next_step in [now + 1, now - 1, now * 2]:
        if 0 <= next_step <= 100000 and (visited[next_step] == -1 or visited[next_step] >= step + 1):
            visited[next_step] = step + 1
            queue.append((next_step, step + 1))

print(min_step)
print(cnt)