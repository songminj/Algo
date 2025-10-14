# 3190번 뱀

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

# 사과 : 1 / 뱀 몸 : -1
for _ in range(K):
    x, y = map(int, input().strip().split())
    board[x-1][y-1] = 1

# 뱀 방향변환 정보
# dir = 0 : 우, 1: 하, 2: 좌, 3: 상
dir = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3:(-1, 0)}
L = int(input())
moves = deque([])
for _ in range(L):
    a, b = input().strip().split()
    moves.append((int(a), b))

snake = deque([])
curr = [0, 0]
board[0][0] = -1
curr_dir = 0
time = 1

while True:
    # 몸길이를 늘려 머리를 다음칸에 위치시킨다
    nx = curr[0] + dir[curr_dir][0]
    ny = curr[1] + dir[curr_dir][1]
    # 벽이나 자신 몸과 부딪히면 끝난다
    if 0 > nx or nx >= N or 0 > ny or ny >= N:
        break
    elif board[nx][ny] < 0:
        break

    if moves and time == moves[0][0]:
        n, d = moves.popleft()
        if d == 'L':
            curr_dir = (curr_dir - 1) % 4
        else:
            curr_dir = (curr_dir + 1) % 4

    snake.append((curr[0], curr[1]))
    # 이동한 칸에 사과가 있다면
    if board[nx][ny] == 0:
        if snake:
            dx, dy = snake.popleft()
            board[dx][dy] = 0
    curr = [nx, ny]
    board[nx][ny] = -1
    time += 1

print(time)