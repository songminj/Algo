import sys
n, k = map(int, sys.stdin.readline().split())

coin = []
for _ in range(n):
    c = int(sys.stdin.readline())
    if c <= k:
        coin.append(c)
    else:
        break

i = 1
cnt = 0
while k > 0:
    if k // coin[-i] == 0:
        i += 1
    cnt += k // coin[-i]
    k = k - (k // coin[-i])*coin[-i]
    i += 1
print(cnt)
