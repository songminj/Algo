import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 피보나치 수를 미리 생성
dp = [1, 2]
while dp[-1] + dp[-2] <= pow(10, 100):
    dp.append(dp[-1] + dp[-2])

def fibo(a, b):
    # a와 b를 정렬하여 범위 보장
    a, b = min(a, b), max(a, b)
    # 이진 탐색으로 범위 내 피보나치 수 계산
    left = bisect_left(dp, a)
    right = bisect_right(dp, b)
    return right - left

def test():
    while True:
        a, b = map(int, input().strip().split())
        if a == 0 and b == 0:
            break
        print(fibo(a, b))

test()
