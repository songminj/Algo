# 1092번 배

import sys
input = sys.stdin.readline

word = input().strip()
n = len(word)
total = [''] * 5

for i in range(n):
    w = word[i]
    if i % 3 == 2:
        t = '*'
    else:
        t = '#'
    total[0] += f'..{t}.'
    total[1] += f'.{t}.{t}'
    if (i> 0) & (i % 3 == 0 ):
        total[2]+= f'*.{w}.'
    else:
        total[2]+= f'{t}.{w}.'
    total[3]+= f'.{t}.{t}'
    total[4]+= f'..{t}.'

    if i == n-1:
        total[0]+='.'
        total[1]+='.'
        total[2]+= f'{t}'
        total[3]+='.'
        total[4]+='.'

for i in range(5):
    print(total[i])