# 2870번 수학숙제

import sys
input = sys.stdin.readline

N = int(input())
nums = []

def makenums(stack):
    tmp = ''.join(stack).lstrip("0")
    if tmp == '':
        nums.append('0')
        return
    nums.append(tmp)

for _ in range(N):
    word = input().strip()
    stack = []
    for w in word:
        # 알파벳에 걸리면 split
        if (ord(w) >= 97 and ord(w) < 123):
            if stack:
                makenums(stack)
                stack.clear()
        else:
            stack.append(w)
    if stack:
        makenums(stack)

nums.sort(key=int)
print(*nums, sep="\n")