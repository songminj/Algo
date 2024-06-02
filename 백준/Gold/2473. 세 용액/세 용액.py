import sys
input = sys.stdin.readline

def find2liqs(now, s, e, i):
    global cnt, res
    while s != e :
        if s == i or e == i:
            return
        if s != i and e != i:
            tmp = [liqs[s], now, liqs[e]]
            sum_tmp = sum(tmp)
            if sum_tmp == 0:
                cnt = 0
                res = tmp
                return
            elif abs(sum_tmp) < abs(cnt):
                cnt = sum_tmp
                res = tmp

            if sum_tmp > 0:
                e -= 1
            elif sum_tmp < 0:
                s += 1


N = int(input())
liqs = list(map(int, input().strip().split()))
liqs.sort()
cnt = 3e9+1
res = [0, 0, 0]
for i in range(1, N-1):
    find2liqs(liqs[i], 0, N-1, i)
    if cnt == 0:
        break
print(*res)
