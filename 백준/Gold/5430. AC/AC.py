import sys

input = sys.stdin.readline
from collections import deque


# R : 배열의 순서를 뒤집음
# D : 첫번째 수를 버린다. 비어있으면 에러

def AC(nums):
    # True이면 정방향, Fasle이면 역방향
    flag = True
    for fx in fxs:
        if fx == 'R':
            if flag:
                flag = False
            else:
                flag = True
        elif fx == 'D':
            if nums:
                if flag:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                return 'error'
    if flag:
        return f"[{','.join(nums)}]"
    else:
        res = []
        while nums:
            res.append(nums.pop())
        return f"[{','.join(res)}]"


T = int(input())
for _ in range(T):
    fxs = input().strip()
    n = int(input())
    arr = list(input().strip()[1:-1].split(','))
    nums = deque()
    for s in arr:
        if s.isdigit():
            nums.append(s)

    print(AC(nums))
