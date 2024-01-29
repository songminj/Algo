#1065. 한수 

num = int(input())

if num < 100:
  cnt = num
else:
  cnt = 99
  for i in range(101, num+1):
    baek = i // 100
    sib = (i // 10) % 10
    il = i % 10
    if baek - sib == sib - il :
      cnt += 1

print(cnt)