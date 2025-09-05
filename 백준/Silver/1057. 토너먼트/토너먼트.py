N, kim, lim = map(int, input().strip().split())
r = 0
while kim != lim:
    kim -= kim // 2
    lim -= lim // 2
    r += 1
print(-1 if r == 0 else r)