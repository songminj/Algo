
n = int(input())

plus = []       # 2~
minus = []      # ~0
one =[]         # 1만 담김
cnt = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        plus += [num]
    elif num < 1:
        minus += [num]
    else:
        one += [num]

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus)//2):
    cnt += plus[i*2] * plus[i*2+1]
for i in range(0, len(minus)//2):
    cnt += minus[i*2] * minus[i*2+1]

if one:
    if len(plus) % 2 == 1 and len(minus) % 2 == 1:
        cnt += sum(one) + plus[-1] + minus[-1]
    elif len(plus) % 2 == 1:
        cnt += sum(one) + plus[-1]
    elif len(minus) % 2 == 1:
        cnt += sum(one) + minus[-1]
    else:
        cnt += sum(one)
else:
    if len(plus) % 2 == 1 and len(minus) % 2 == 1:
        cnt += minus[-1] + plus[-1]
    elif len(plus) % 2 == 1:
        cnt += plus[-1]
    elif len(minus) % 2 == 1:
        cnt += minus[-1]

print(cnt)