import sys
test_case = int(sys.stdin.readline())

ns = [0] * 12
ns[1] = 1
ns[2] = 2
ns[3] = 4

for i in range(test_case):
    n = int(sys.stdin.readline())
    if n > 3:
        for j in range(4, n+1):
            ns[j] = ns[j-1] + ns[j-2] + ns[j-3]
    print(ns[n])