# 7523번 Gauß

import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
    n, m = map(int, input().strip().split())
    print(f'Scenario #{i}:\n{((n+m) * (m-n+1))//2}\n')