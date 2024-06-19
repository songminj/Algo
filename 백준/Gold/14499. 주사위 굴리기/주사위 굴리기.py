# 14499번 주사위 굴리기

"""
주사위를 굴렸을 때
이동한 칸 숫자 == 0이면
주사위의 바닥면 숫자가 칸으로 복사

이동한 칸 숫자 != 0이면
이동한 칸 숫자가 주사위로 복사.
칸 숫자 = 0

"""

n, m, x, y, k = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(n)]
orders = list(map(int, input().strip().split()))
# 동, 서, 북, 남 순서
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, 0, 0, 0, 0, 0]

def roll(k):
    # 동쪽일 때
    tmp = dice[:]
    if k == 1:
        dice[1] = tmp[5]
        dice[2] = tmp[1]
        dice[3] = tmp[2]
        dice[5] = tmp[3]
    # 서쪽일 때
    elif k ==2:
        dice[1] = tmp[2]
        dice[2] = tmp[3]
        dice[3] = tmp[5]
        dice[5] = tmp[1]
    # 북쪽일 때
    elif k ==3:
        dice[0] = tmp[5]
        dice[2] = tmp[0]
        dice[4] = tmp[2]
        dice[5] = tmp[4]
    # 남쪽일때
    else:
        dice[0] = tmp[2]
        dice[2] = tmp[4]
        dice[4] = tmp[5]
        dice[5] = tmp[0]


for i in orders:
    dx = x + delta[i-1][0]
    dy = y + delta[i-1][1]
    if 0 <= dx < n and 0 <= dy < m:
        roll(i)
        if arr[dx][dy] == 0:
            arr[dx][dy]= dice[5]
        else:
            dice[5] = arr[dx][dy]
            arr[dx][dy] = 0
        print(dice[2])
        x, y = dx, dy
