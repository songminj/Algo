# 1730번 판화

import sys
input = sys.stdin.readline

N = int(input())
robot = input().strip()
moves = len(robot)
code = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def carve():
    x, y = 0, 0
    idx = 0
    vertical = [[0] * N for _ in range(N)]
    horizontal = [[0] * N for _ in range(N)]
    while idx < moves:
        c = robot[idx]
        nx = x + code[c][0]
        ny = y + code[c][1]
        if 0 <= nx < N and 0 <= ny < N:
            if c in 'UD':
                vertical[x][y] = 1
                vertical[nx][ny] = 1
            else:
                horizontal[x][y] = 1
                horizontal[nx][ny] = 1
            x = nx
            y = ny
        idx += 1
    for i in range(N):
        for j in range(N):
            if vertical[i][j] and horizontal[i][j]:
                print('+', end='')
            elif vertical[i][j]:
                print('|', end='')
            elif horizontal[i][j]:
                print('-', end='')
            else:
                print('.', end='')
        print('', end='\n')
    return

carve()