import sys

# 
# def binary_search(target):
#     start = 0
#     end = len(s_nums) - 1
#     while start <= end:
#         mid = (start + end) // 2
# 
#         if s_nums[mid] == target:
#             return mid
#         elif s_nums[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
s_nums = sorted(list(set(nums)))
dic = {s_nums[i]: i for i in range(len(s_nums))}

for i in nums:
    print(dic[i], end=' ')

# print(sort_nums)
