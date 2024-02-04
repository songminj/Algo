# N , M  : 행렬의 크기 

N, M = map(int, input().split())
arr1 = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]
cnt = 0

for i in range(N-2):
  for j in range(M-2):
    if arr1[i][j] != arr2[i][j] :
      cnt += 1
      for k in range(3):
        for l in range(3):
          if arr1[i+k][j+l] == 1:
            arr1[i+k][j+l] = 0
          else :
            arr1[i+k][j+l] = 1

if arr1 != arr2:
  print(-1)
else: 
  print(cnt)   