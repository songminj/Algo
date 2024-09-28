# 17256 나의 인생에는 수학과 함께

import sys
input = sys.stdin.readline

N = int(input())
delta = [(0, 1), (1, 0)]
board = [list(input().strip().split()) for _ in range(N)]

max_val, min_val = float('-inf'), float('inf')
endpoint = 2*N -1

def checkboundary(x, y):
    if (0 <= x < N ) and (0 <= y < N):
        return True
    else:
        return False
def moving(x, y, val):
    global max_val, min_val
    if x == N-1 and y == N-1:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    for i in range(2):
        dx = x + delta[i][0]
        dy = y + delta[i][1]
        if checkboundary(dx, dy):
            for i in range(2):
                kx = dx + delta[i][0]
                ky = dy + delta[i][1]
                if checkboundary(kx, ky):
                    expression = f'{val} {board[dx][dy]} {board[kx][ky]}'
                    tmp = eval(expression)
                    moving(kx, ky, tmp)
moving(0, 0, int(board[0][0]))
print(max_val, min_val)
