# 20291 파일정리 

import sys
input = sys.stdin.readline

t = int(input())
# 개수를 저장
ex_cnt = dict()

for _ in range(t):
    _, ex = input().strip().split('.')
    ex_cnt[ex] = ex_cnt.get(ex, 0) + 1

ex_ord = sorted(ex_cnt.keys())

for w in ex_ord:
    print(w, ex_cnt[w])