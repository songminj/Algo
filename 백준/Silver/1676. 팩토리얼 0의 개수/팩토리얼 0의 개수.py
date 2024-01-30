num = int(input())
cnt = 0

if num == 0 :
  cnt = 0
else :
  range_num = list(range(1, num+1))
  for i in range_num:
    if i % 5 == 0:
      cnt += 1
      if (i // 5) % 5 == 0:
        cnt += 1
        if (i //25 ) % 5 == 0:
          cnt += 1

print(cnt)