# 명령 프롬프트
import sys

file = int(sys.stdin.readline())
search = list(map(str, sys.stdin.readline()))
for _ in range(file-1):
  name = list(map(str, sys.stdin.readline()))
  for i in range(len(search)):
    if search[i] != name[i]:
      search[i] = '?'
print(''.join(search))