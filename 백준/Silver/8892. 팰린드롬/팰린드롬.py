import sys

input = sys.stdin.readline

tc = int(input())

def solve(n : int, words: list):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      word= words[i] + words[j]
      if word == word[::-1]:
        return word
  return 0
      
for _ in range(tc):
  k = int(input())
  words = list(input().strip() for _ in range(k))
  print(solve(n=k, words=words))