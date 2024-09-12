# 암호해독기

import sys
input = sys.stdin.readline

N = int(input())
code = list(map(int, input().strip().split()))
dec = input().strip()
dec_set = {}
for d in dec:
    dec_set[d] = dec_set.get(d, 0) + 1

for c in code:
    if 1<= c < 27:
        dec_set[chr(c+64)] = dec_set.get(chr(c+64), 0) - 1
    elif 27 <= c:
        dec_set[chr(c+70)] = dec_set.get(chr(c+70), 0) - 1
    else:
        dec_set[' '] = dec_set.get(' ', 0) - 1

for k, v in dec_set.items():
    if v != 0:
        print('n')
        break
else:
    print('y')
