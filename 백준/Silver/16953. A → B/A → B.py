a, b = map(int, input().split())

def dfs(a, b, t):
    global lst
    if a >= b:
        if a == b:
            lst.append(t)
            return
        else:
            return
    for i in range(2):
        if i:
            dfs(a*2, b, t+1)
        else:
            dfs(10*a+1, b, t+1)

lst = []
dfs(a, b, 1)
if lst:
    print(sorted(lst)[-1])
else:
    print(-1)
