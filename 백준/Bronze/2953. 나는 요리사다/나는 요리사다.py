res = 0
man = 0
for i in range(1, 6):
    point = sum(list(map(int, input().split())))
    if point > res:
       res = point
       man = i
print(man, res)