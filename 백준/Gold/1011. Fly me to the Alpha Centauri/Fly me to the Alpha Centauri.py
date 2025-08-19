import sys
input = sys.stdin.readline

T = int(input())

def alpha_centauri(x: int, y: int):
    dist = y - x
    moved = 0
    cnt = 0
    repeatable = 0

    while moved < dist:
        cnt += 1
        if cnt % 2 == 1:
            repeatable +=1
        moved += repeatable

    return cnt

for _ in range(T):
    x, y = map(int, input().strip().split())
    print(alpha_centauri(x, y))