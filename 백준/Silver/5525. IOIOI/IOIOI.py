p = 'IO' * int(input())+'I'
s_len = int(input())
s = input()
cnt = 0

for i in range(s_len - len(p)+1):
    if s[i] == 'I':
        for j in range(1, len(p)):
            if p[j] != s[i+j]:
                break
        else :
            cnt += 1
print(cnt)