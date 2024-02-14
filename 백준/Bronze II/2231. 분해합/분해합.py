import sys

num = int(sys.stdin.readline().strip())
num_len = len(str(num))
min_sum = num

if int(num) >= (num_len*9):
    for i in range(num-(num_len*9)-1, num):
        each = list(map(int, str(i)))
        if (i + sum(each)) == num:
            min_sum = i
            break
else:
    for i in range(1, num):
        each = list(map(int, str(i)))
        if (i + sum(each)) == num:
            min_sum = i
            break
if min_sum == num:
    print(0)
else:
    print(min_sum)