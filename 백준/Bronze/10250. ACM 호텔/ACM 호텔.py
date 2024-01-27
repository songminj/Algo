test_case = int(input())

for i in range(test_case):
  h, w, n = map(int, input().split())
  # 101 부터 차례대로

  if n % h == 0 :
    xx = str(n // h)
    yy = str(h)
  else :
    xx = str(n // h + 1)
    yy = str(n % h)

  if len(xx) == 1:
    xx = '0'+ xx

  print(yy+xx)