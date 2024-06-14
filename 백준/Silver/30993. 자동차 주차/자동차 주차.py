# 30993번 자동차 주차

n, *color = map(int, input().strip().split())
res = 0
def comb(k, col):
    global res
    if k == n:
        res += 1
    for i in range(3):
        if color[i] > 0:
            col[i] -= 1
            comb(k+1, col)
            col[i] += 1
comb(0, color)
print(res)