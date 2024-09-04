# 31908번 커플링매치

n = int(input())
ring = {}
for _ in range(n):
    name, style = input().strip().split()
    if style != '-':
        ring[style] = ring.get(style, []) + [name]
ans = ''
cnt = 0
for k, v in ring.items():
    if len(v) == 2:
        ans +=f'\n{" ".join(v)}'
        cnt += 1

print(cnt)
print(ans)