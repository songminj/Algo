# 2631번 줄세우기

N = input()
arr = [0] * 10
for i in N:
    n = int(i)
    arr[n] += 1
for i in range(9, -1, -1):
    if arr[i]:
        print(str(i) * arr[i],end='')