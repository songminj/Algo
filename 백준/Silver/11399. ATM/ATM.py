import sys

person = int(sys.stdin.readline().rstrip())
time = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(person-1, 0, -1):
    for j in range(i):
        if time[j] > time[j+1]:
            time[j], time[j+1] = time[j+1], time[j]
total = 0
for i in range(person):
    total += time[i]*(person-i)

print(total)
