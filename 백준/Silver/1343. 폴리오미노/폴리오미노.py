import sys
input = sys.stdin.readline

poly = input().strip().split('.')
res = []
for p in poly:
    if len(p) % 2 == 1:
        print(-1)
        break
    else:
        tmp = 'AAAA' * (len(p) // 4) + 'BB' * (1 if ((len(p) % 4 ) == 2) else 0)
        res.append(tmp)
else:
    print('.'.join(res))