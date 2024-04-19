import sys
input = sys.stdin.readline

word = input().strip()
arr = [0] * 26
for w in word:
    arr[ord(w)-97] += 1
print(*arr)