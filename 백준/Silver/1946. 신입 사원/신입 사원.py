import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # 정렬을 해주고
    rank = [tuple(map(int, input().split())) for _ in range(N)]
    rank.sort()

    # 회의실 배정 문제처럼
    s, res = 0, 1
    for i in range(1, N):
        if rank[i][1] < rank[s][1]:
            s = i
            res += 1
    print(res)