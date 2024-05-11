L, P = map(int, input().split())
popu = L*P
pt = list(input().split())
res = ''

for i in pt:
    res += str(int(i)- popu) + ' '

print(res)