import sys
input = sys.stdin.readline

T = int(input())

def turret(x1, y1, r1, x2, y2, r2):
    # 백과 조의 위치가 같으면서
    if (x1 == x2) and (y1 == y2):
        if r1 != r2:
            return 0
        return -1
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 in ((r1 - r2)**2, (r1 + r2)**2) :
        return 1
    if (r1 - r2)**2 < (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2)**2 :
        return 2
    return 0

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    print(turret(x1, y1, r1, x2, y2, r2))