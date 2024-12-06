# 32292번 ABB to BA

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    S = input().strip()
    while True:
        if 'ABB' in S:
            S = S.replace('ABB', 'BA')
        else:
            break
    print(S)