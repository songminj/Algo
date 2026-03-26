# 2357번 오렌지먹은지오랜지

import sys
input = sys.stdin.readline

N = int(input())
word = input().strip()

def orange(word, N):
    for i in range(1, N):
        a, b = word[:i], word[N-i:]
        flag = 0
        for j in range(i):
            if a[j] != b[j]:
                flag +=1
        if flag == 1:
            return "YES"
    else:
        return "NO"
print(orange(word, N))