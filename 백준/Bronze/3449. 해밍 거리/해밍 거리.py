# 3449번 해밍거리

import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    a = int(input(), 2)
    b = int(input(), 2)
    t = bin(a ^ b).count('1')
    print(f"Hamming distance is {t}.")