# 1316 그룹 단어 체커

import sys
input = sys.stdin.readline

N = int(input())

def group_check(word : str):
    stack = []
    is_existed = [0] * 26
    for w in word:
        n = ord(w) - 97
        if len(stack) == 0:
            # 단어가 이미 나왔던거라면
            if is_existed[n]:
                return 0
            stack.append(w)
            is_existed[ord(w)-97] += 1
        else:
            if is_existed[n] and stack[-1] != w:
                return 0
            if stack[-1] == w:
                continue
            else:
                stack.pop()
                stack.append(w)
                is_existed[ord(w) - 97] += 1
    return 1

ans = 0
for _ in range(N):
    word = input().strip()
    ans += group_check(word)
print(ans)