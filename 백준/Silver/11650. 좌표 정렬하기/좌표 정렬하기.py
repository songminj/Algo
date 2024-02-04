# N: 점의 개수 
N = int(input())

lst = []
for _ in range(N):
  point = tuple(map(int, input().split()))
  lst.append(point)

lst.sort()
for i in range(N):
  print(*lst[i])