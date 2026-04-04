# 30470번 호반우가 학교에 지각한 이유 3

import sys
input = sys.stdin.readline

N = int(input())

stack = []
total = 0

for _ in range(N):
    a, b = map(int, input().split())

    if a == 1:
        stack.append((b, 1))
        total += b
    else:
        if not stack:
            continue
        k = stack[-1][0]
        t = max(k - b, 0)
        cnt = 0

        while stack and stack[-1][0] >= t:
            val, c = stack.pop()
            total -= val * c
            cnt += c

        if cnt > 0:
            stack.append((t, cnt))
            total += t * cnt

print(total)