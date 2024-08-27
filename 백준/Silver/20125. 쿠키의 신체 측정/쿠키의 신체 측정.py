# 20125번 쿠키의 신체 측정

import sys
input = sys.stdin.readline

n = int(input())
cookie = [list(input().strip()) for _ in range(n)]

# 심장 찾기
def find_heart():
    for i in range(n):
        for j in range(n):
            if cookie[i][j] == '*':
                print(i+2, j+1)
                return i+1, j

heart_x, heart_y = find_heart()

# 신체부위
def body(hx, hy, dx, dy):
    cnt = 0
    while True:
        hx = hx+dx
        hy = hy+dy
        if 0<= hx < n and 0 <= hy < n and cookie[hx][hy] == "*":
            cnt += 1
        else:
            break
    print(cnt, end=" ")
    return cnt

for dx, dy in [(0, -1), (0, 1)]:
    body(heart_x, heart_y, dx, dy)
waist = body(heart_x, heart_y, 1, 0)
body(heart_x+waist, heart_y-1, 1, 0)
body(heart_x+waist, heart_y+1, 1, 0)