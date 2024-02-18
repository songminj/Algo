# n : 시험장 개수
n = int(input())
# 시험장의 응시자수
pops = list(map(int, input().split()))
# b : 총감독관, c : 부감독관
b, c = map(int, input().split())
cnt = 0
for i in range(n):
    left = pops[i] - b
    cnt += 1
    if left > 0:
        if left % c == 0:
            cnt += left // c
        else:
            cnt += left // c + 1

print(cnt)