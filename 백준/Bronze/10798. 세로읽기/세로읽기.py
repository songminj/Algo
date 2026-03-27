# 10789번 세로읽기

import sys
input = sys.stdin.readline

code = [list(input().strip()) for _ in range(5)]

for i in range(5):
    code[i] = code[i] + [''] * (15-len(code[i]))

for lst in list(zip(*code)):
    print(''.join(lst), end='')