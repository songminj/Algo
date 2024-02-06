# 회원수 
n = int(input())
people = list()

for i in range(n):
    a, b = input().split()
    people.append([int(a), b])
people.sort(key = lambda x : x[0], reverse=False)

for i in range(n):
    print(*people[i], end='\n')