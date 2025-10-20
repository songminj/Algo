import sys
input = sys.stdin.readline

t = int(input())

def candy(board, n, shape):
  cnt = 0
  for i in range(n):
    cnt += len(''.join(board[i]).split(shape)) -1
  return cnt

for _ in range(t):
  input()
  ans = 0
  r, c = map(int, input().split())
  arr = [list(input().strip()) for _ in range(r)]
  ans += candy(arr, r, '>o<')
  ans += candy(list(zip(*arr)), c, 'vo^')
  print(ans)