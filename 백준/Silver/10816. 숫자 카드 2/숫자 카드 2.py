import sys

# n : card
n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))

# target num
tnum = int(sys.stdin.readline().strip())
targets = list(map(int, sys.stdin.readline().strip().split()))
targets_count = {i: 0 for i in targets}

res = []
# counting
for i in range(n):
    if cards[i] in targets_count.keys():
        targets_count[cards[i]] += 1
for i in targets:
    res.append(targets_count[i])
print(*res)