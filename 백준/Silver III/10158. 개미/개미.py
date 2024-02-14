import sys
# w, h : 가로 세로
w, h = map(int, sys.stdin.readline().strip().split())
# 개미 처음 위치
x, y = map(int, sys.stdin.readline().strip().split())
# t초
t = int(sys.stdin.readline())

turn_x, more_x = divmod(t, 2*w)
turn_y, more_y = divmod(t, 2*h)
# print(turn_x, more_x)
# print(turn_y, more_y)

if (more_x + x) // w % 2 == 1:
    # 한번 튕겨서 내 위치가 -방향
    result_x = 2* w - (more_x + x)
else :
    result_x = (more_x + x) % w

if (more_y + y) // h% 2 == 1:
    # 한번 튕겨서 내 위치가 -방향
    result_y = 2* h - (more_y + y)
else :
    result_y = (more_y + y) % h

print(result_x, result_y)
