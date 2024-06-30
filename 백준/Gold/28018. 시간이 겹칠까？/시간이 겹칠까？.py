import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
student = [tuple(map(int, input().strip().split())) for _ in range(N)]
Q = int(input())
time = list(map(int, input().strip().split()))

# 누적합을 기록할 배열을 만든다
record = [0] * 1000002

for s, e in student:
    record[s] += 1
    record[e+1] -= 1

for i in range(1, 1000002):
    record[i] += record[i-1]

for t in time:
    print(record[t])