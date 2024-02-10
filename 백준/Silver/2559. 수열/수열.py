import sys

# n: 온도를 측정한 날짜의 수 k: 얼마나 합할건지
n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
max_temp, sum_temp = 0, 0

for i in range(k):
    sum_temp += temp[i]
max_temp = sum_temp

for j in range(0, n-k):
    if j+k < n:
        sum_temp += temp[j+k]
    sum_temp -= temp[j]
    if max_temp < sum_temp:
        max_temp = sum_temp

print(max_temp)