# 11008번 복붙의 달인

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s, p = input().strip().split()
    ans = s.count(p)

    splited = s.split(p)
    for word in splited:
        if word != '':
            ans += len(word)
    print(ans)