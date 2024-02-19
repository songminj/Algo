# 백준 9375

import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    dic = {}
    # number
    n = int(sys.stdin.readline())
    for _ in range(n):
        clothes, key = map(str, sys.stdin.readline().split())
        dic.setdefault(key, [])
        dic[key] += [clothes]

    cnt = 1
    for v in dic.values():
        cnt *= (len(v)+1)
    print(cnt-1)

