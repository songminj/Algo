import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
  order = sys.stdin.readline().split()
  if 'push' in order:
    stack.append(order[1])
    continue
  elif 'pop' in order:
    if len(stack) != 0:
      popnum = stack.pop()
      print(popnum)
      continue
    else :
      print(-1)
      continue
  elif 'size' in order:
    print(len(stack))
    continue
  elif 'empty' in order:
    if len(stack) != 0:
      print(0)
      continue
    else:
      print(1)
  elif 'top' in order:
    if len(stack) != 0:
      print(stack[-1])
    else :
      print(-1)
