# 28238번 정보 선생님의 야망

import sys
input = sys.stdin.readline

n = int(input())
# 0~4 : 월~금
schedule = {i : set() for i in range(5)}

for k in range(n):
    times = list(map(int, input().strip().split()))
    for t in range(5):
        if times[t]:
            schedule[t].add(k)
max_val = 0

for i in range(4):
    for j in range(i+1, 5):
        cnt = len(schedule[i] & schedule[j])
        if max_val <= cnt:
            max_val = cnt
            res = ['0', '0', '0', '0', '0']
            res[i] = '1'
            res[j] = '1'
print(max_val, ' '.join(res), sep="\n")