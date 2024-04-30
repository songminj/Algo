import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

while True:
    if E == S and S == M :
        break
    if min(E, S, M) == E:
        E += 15
    elif min(E, S, M) == S:
        S += 28
    else:
        M += 19
print(E)
