#2577 
a = int(input())
b = int(input())
c = int(input())

total = str(a*b*c)
nums = list(map(str, range(10)))
for i in nums:
  print(total.count(i))