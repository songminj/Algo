# 2495번 연속구간

import sys

input = sys.stdin.readline

def check(num):
    stack = []
    res = 1
    cnt = 0
    for n in num:
        if not stack:
            stack.append(n)
            cnt += 1
        else:
            if stack[-1] == n:
                cnt += 1
            else:
                stack.pop()
                stack.append(n)
                res = max(cnt, res)
                cnt = 1

    return max(res, cnt)

for _ in range(3):
    nums = input()
    print(check(nums))