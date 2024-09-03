# 7490번 0만들기

tc= int(input())

def makeZero(func, step):
    if step == n:
        cnt = eval(func.replace(' ',''))
        if cnt == 0:
            print(func)
        return
    step += 1

    makeZero(func+' '+str(step), step)
    makeZero(func+'+'+str(step), step)
    makeZero(func+'-'+str(step), step)

for _ in range(tc):
    n = int(input())
    total = sum(range(1, n+1))
    makeZero('1', 1)
    print()