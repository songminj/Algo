import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(input().strip())
stack = []

for n in nums:
    while stack and stack[-1] < n and K >0:
        stack.pop()
        K -= 1
    stack.append(n)
if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))