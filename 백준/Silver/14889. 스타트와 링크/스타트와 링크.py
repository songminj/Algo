import sys
from itertools import combinations
input = sys.stdin.readline

def perm(lst):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            x, y = lst[i], lst[j]
            cnt += arr[x][y] + arr[y][x]
    return cnt
res = 1e9
N= int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
n = N//2
nums = [i for i in range(1, N)]

for t in combinations(nums, N-n-1):
    teams = [0]
    teams.extend(t)
    others = [ i for i in range(1, N) if i not in teams]
    a, b = perm(teams), perm(others)
    diff = abs(a-b)
    if diff < res:
        res = diff

print(res)