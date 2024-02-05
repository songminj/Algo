# n : 세로 , m : 가로 
n, m = map(int, input().split())

# 판 읽어오기 

arr = [list(map(str, input())) for _ in range(n)]

cnt = 0
for i in range(n-7):
  for j in range(m-7):
    black = 0
    for a in range(8):
      for b in range(8):
        if (a+b) % 2 == 0:
          black += (arr[a+i][b+j] == "B")
        else :
          black += (arr[a+i][b+j] == "W")

    if black < 32:
      black = 64 - black
    if cnt < black :
      cnt = black
print(64-cnt) 