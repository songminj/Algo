import sys
input = sys.stdin.readline

n = int(input())
string = input().strip()
tmp = 0
for i in range(n):
    tmp += (ord(string[i])-96) * (31**i)

print(tmp%1234567891)
