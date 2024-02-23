num = int(input())

numlast = int(num ** (1/2))
dp = set()
for i in range(1, numlast+1):
    dp.add(i**2)
# print(dp)
def lagr(num):
    for i in range(numlast, 0, -1):
        if i**2 == num :
            return 1
        elif num - i**2 in dp:
            return 2
    for i in range(numlast, 0, -1):
            for j in range(numlast, 0, -1):
                if num - i**2 - j**2 in dp:
                    return 3
    return 4

print(lagr(num))