# 16719번 ZOAC


import sys
input = sys.stdin.readline

word = list(input().strip())
res = ['']*len(word)

def zoac(word, s):
    if not word:
        return
    mn = min(word)
    idx = word.index(mn)
    res[s+idx] = mn
    print(''.join(res))
    zoac(word[idx+1:], s+idx+1)
    zoac(word[:idx], s)

zoac(word, 0)