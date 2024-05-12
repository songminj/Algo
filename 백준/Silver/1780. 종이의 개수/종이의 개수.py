import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = {-1: 0, 0: 0, 1: 0}


def find(x, y, p):
    global res
    tg = arr[x][y]
    for i in range(x, p + x):
        for j in range(y, p + y):
            if arr[i][j] != tg:
                smaller = p // 3
                find(x, y, smaller)
                find(x, y + smaller, smaller)
                find(x, y + 2 * (smaller), smaller)
                find(x + smaller, y, smaller)
                find(x + smaller, y + smaller, smaller)
                find(x + smaller, y + 2 * (smaller), smaller)
                find(x + 2 * (smaller), y, smaller)
                find(x + 2 * (smaller), y + smaller, smaller)
                find(x + 2 * (smaller), y + 2 * (smaller), smaller)
                return
    else:
        if tg == 1:
            res[1] += 1
        elif tg == -1:
            res[-1] += 1
        else:
            res[0] += 1


find(0, 0, n)

for key, value in res.items():
    print(value)