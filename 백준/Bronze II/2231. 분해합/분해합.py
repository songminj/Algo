import sys

num = int(sys.stdin.readline().strip())
num_len = len(str(num))
min_sum = num

if int(num) >= (num_len*9):
    rg = range(num-(num_len*9)-1, num)
else:
    rg = range(1, num)

for i in rg:
    each = list(map(int, str(i)))
    if (i + sum(each)) == num:
        min_sum = i
        break

if min_sum == num:
    print(0)
else:
    print(min_sum)