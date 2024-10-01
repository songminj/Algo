# 1062 가르침

import sys
from itertools import combinations

input = sys.stdin.readline

def cnt_readible(learned, words):
    cnt = 0
    for word in words:
        if word & learned == word:
            cnt += 1
    return cnt

def readable():
    teached = {'a', 'n', 't', 'i', 'c'}
    words = []

    for _ in range(N):
        word = input().strip()
        bitmask = 0
        for w in set(word) - teached:
            bitmask |= (1 << (ord(w) - 97))
        words.append(bitmask)

    learned= 0
    for t in teached:
        learned |= (1 << (ord(t) - 97))

    more = set(chr(i + ord('a')) for i in range(26)) - teached

    ans = 0
    for comb in combinations(more, K-5):
        tmp = learned
        for c in comb:
            tmp |= (1 << (ord(c) - 97))

        ans = max(ans, cnt_readible(tmp, words))
    print(ans)


N, K = map(int, input().strip().split())

if K < 5:
    print(0)
else:
    readable()