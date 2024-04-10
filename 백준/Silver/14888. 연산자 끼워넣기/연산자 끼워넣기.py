import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
pdt = list(map(int, input().strip().split()))
pdt_num = sum(pdt)
visited = [0, 0, 0, 0]
res = nums[0]

max_res, min_res = -1e10, 1e10
def products(k, x, a):
    # 덧셈
    if k == 0:
        return x+a
    # 뻴셈
    if k == 1:
        return x-a
    # 곱셈
    if k == 2:
        return x * a
    # 나눗셈
    if k == 3:
        if x < 0:
            x = -x
            return -(x//a)
        return x //a

def cal(idx, res):
    global visited, max_res, min_res
    if idx == pdt_num:
        if res > max_res:
            max_res = res
        if res < min_res:
            min_res = res
        return
    for i in range(4):
        if pdt[i] > 0 and pdt[i] > visited[i]:
            visited[i] += 1
            tmp = products(i, res, nums[idx+1])
            cal(idx+1, tmp)
            visited[i] -= 1

cal(0, res)
print(max_res)
print(min_res)