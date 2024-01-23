friend = 1
while friend > 0 :
  m, f = map(int, input().split())
  friend = m+f
  if friend == 0:
    break
  print(m+f)
