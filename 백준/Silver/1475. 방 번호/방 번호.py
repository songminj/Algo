import sys

n = sys.stdin.readline().strip()
nums = [0] * 10
sixnine = 0
for number in n:
    k = int(number)
    if k == 9 or k == 6:
        sixnine += 1
    else:
        nums[k] += 1

print(max(max(nums), (sixnine+1) // 2))