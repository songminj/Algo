# 10996번 별찍기 - 21

N = int(input())

def star(n):
    if n % 2 ==0:
        iseven = True
    else:
        iseven = False
    for i in range(2*n):
        if i % 2 == 0:
            if iseven:
                print('* ' * (n//2))
            else:
                print('* '*(n//2)+'*')

        else:
            if iseven:
                print(' *' * (n//2))
            else:
                print(' *' * (n//2)+' ')

if N == 1:
    print('*')
else:
    star(N)