# 2661번 좋은수열

N = int(input())

def check(isseq, length):
    for idx in range(1, length//2+1):
        if isseq[-idx:] == isseq[-(idx*2):-idx]:
            return False
    else:
        return True

def goodseq(l, t):
    if t == N:
        print(l)
        exit()
    for nxt in '123':
        if check(l+str(nxt), t+1):
            goodseq(l+str(nxt), t+1)

goodseq('1', 1)