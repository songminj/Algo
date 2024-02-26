# 3986. 좋은 단어
import sys

# 좋은 단어의 수
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    stack = []
    string = map(str, sys.stdin.readline().strip())

    for w in string:
        if stack:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)
    # print(stack)
    if not stack:
        cnt += 1

print(cnt)

