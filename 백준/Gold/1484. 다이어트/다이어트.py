# 1484번 다이어트

G = int(input())

l, r = 1, 2
ans = []
while True:
    diff = (r**2) - (l ** 2)
    if r > 50000:
        break
    if diff < G:
        r += 1
        continue
    elif diff > G:
        l += 1
        continue
    elif diff == G:
        ans.append(str(r))
        r += 1
        continue
if ans:
    print('\n'.join(ans))
else:
    print(-1)