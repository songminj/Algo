import sys
n = int(sys.stdin.readline())

queue = []
for _ in range(n):
  order = sys.stdin.readline().split()

  if 'push' in order:
    queue.append(order[1])
    continue
  elif 'pop' in order:
    if len(queue) != 0:
      popnum = queue.pop(0)
      print(popnum)
      continue
    else :
      print(-1)
      continue
  elif 'size' in order:
    print(len(queue))
    continue
  elif 'empty' in order:
    if len(queue) != 0:
      print(0)
      continue
    else:
      print(1)
  elif 'front' in order:
    if len(queue) != 0:
      print(queue[0])
    else:
      print(-1)
  elif 'back' in order:
    if len(queue) != 0:
      print(queue[-1])
      continue
    else :
      print(-1)
      continue
