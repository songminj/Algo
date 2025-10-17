import sys
input = sys.stdin.readline

n = int(input())
ans = 0
skylines = [int(input().strip().split()[1]) for _ in range(n)]
skylines.append(0)
stack = [0]

for p in skylines:
    h = p
    while stack[-1] > p:
        if stack[-1] != h:
            ans += 1
            h = stack[-1]
        stack.pop()
    stack.append(p)
print(ans)