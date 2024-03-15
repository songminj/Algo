import sys

n = int(sys.stdin.readline())
people = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]

people_sort = sorted(people[:], key= lambda x: (x[0], x[1]), reverse=True)
for i in range(n):
    k, cnt = 0, 1
    while people_sort[k][0] > people[i][0]:
        if people_sort[k][1] > people[i][1]:
            cnt += 1
        k += 1
    print(cnt, end=' ')
