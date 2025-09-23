import sys

code = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()

m = len(code)
n = len(target)

idx = 0
count = 0

while idx <= m - n:
    if code[idx:idx+n] == target:
        count += 1
        idx += n
    else:
        idx += 1

print(count)