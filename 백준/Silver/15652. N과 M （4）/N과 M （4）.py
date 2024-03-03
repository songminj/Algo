# n 과 m (4)
# 1부터 n까지중에 m개 뽑음
n, m = map(int, input().split())

def perm(start, m, lst):
    if len(lst) == m:
        print(*lst)
        return
    # 1부터 n까지 탐색
    for i in range(start, n+1):
        perm(i, m, lst+[i])

perm(1, m, [])