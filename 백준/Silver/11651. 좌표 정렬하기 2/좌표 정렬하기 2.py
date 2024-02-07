n = int(input())
di = []
for _ in range(n):
    point = list(map(int, input().split()))
    di.append(point)

di.sort(key= lambda x : (x[1], x[0]))

for i in range(n):
    print(*di[i])