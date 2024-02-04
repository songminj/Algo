# N: 점의 개수 
N = int(input())

position = [list(map(int, input().split())) for _ in range(N)]

position.sort(key = lambda x : (x[0], x[1]))
for it in position:
  print(*it)