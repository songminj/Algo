import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0, 1, 2, 3 = 북, 동, 남, 서 / 내가 서있는 방향 기준
drc = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
clean = 0


def vacuum(r, c, d):
    global clean, arr
    if arr[r][c] == 0:
        clean += 1
        arr[r][c] = -1

    flag = False
    for i in range(4):
        nr = r + delta[i][0]
        nc = c + delta[i][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            flag = True

    if flag:
        cnt = 0
        while True:
            if cnt == 4:
                break
            new_d = (d + 3 - cnt) % 4
            kr = r + drc[new_d][0]
            kc = c + drc[new_d][1]
            if 0 <= kr < N and 0 <= kc < M and arr[kr][kc] == 0:
                vacuum(kr, kc, new_d)
                return
            cnt += 1

    if not flag:
        pr = r - drc[d][0]
        pc = c - drc[d][1]
        if 0 <= pr < N and 0 <= pc < M and arr[pr][pc] != 1:
            vacuum(pr, pc, d)
            return

vacuum(r, c, d)
print(clean)
