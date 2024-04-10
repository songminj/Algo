import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
NGE = ['-1'] * N
# index를 stack에 넣는다
stack = [0]
for i in range(1, N):
    # 왼쪽에서 큰 수가 나올 때 까지 while문을 돌린다
    while stack and nums[stack[-1]] < nums[i]:
        NGE[stack.pop()] = str(nums[i])
    stack.append(i)
print(' '.join(NGE))
