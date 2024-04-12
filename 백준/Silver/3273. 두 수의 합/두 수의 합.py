import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
res = 0
s, e = 0, n-1
while True:
    if s >= e:
        break
    tmp = arr[s] + arr[e]
    if tmp == X:
        res += 1
        s += 1
        e -= 1
    elif tmp < X:
        s += 1
    else:
        e -= 1
print(res)