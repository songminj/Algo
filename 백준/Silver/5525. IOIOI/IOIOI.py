import sys
p = int(sys.stdin.readline())
s_len = int(sys.stdin.readline())
s = sys.stdin.readline()

i, cnt, result = 0, 0, 0
while i < (s_len-1):
    if s[i:i+3] == "IOI":
        cnt += 1
        i += 2
        if cnt == p:
            result += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(result)