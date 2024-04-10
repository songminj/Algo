import sys

input =sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = sorted([input().strip() for _ in range(n)])
    for i in range(n-1):
        if numbers[i+1].startswith(numbers[i]):
            print('NO')
            break
    else:
        print('YES')