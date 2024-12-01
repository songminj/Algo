import sys
input = sys.stdin.readline

N = int(input())

total = []
for _ in range(N):
    name, ko, en, mat = input().strip().split()
    ko = int(ko)* -1
    en = int(en) 
    mat = int(mat)* -1
    total.append([name, ko, en, mat])

total.sort(key=lambda x: (x[1], x[2], x[3], x[0]))
for i in range(N):
    print(total[i][0])