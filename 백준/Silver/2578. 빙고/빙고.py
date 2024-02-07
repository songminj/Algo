cs = [list(map(int, input().split())) for _ in range(5)]
number = []
for _ in range(5):
    number += list(map(int, input().split()))
# list comprehension으로 한줄로 만들어주기
# number = [data for inner in number for data in inner]
cnt = 0

for i in range(25):
    bingo = 0
    for r in range(5):
        for c in range(5):
            if cs[r][c] == number[i]:
                cs[r][c] = 0
                cnt += 1

    if cnt >= 11:
        # 가로 합
        for j in range(5):
            if sum(cs[j]) == 0:
                bingo += 1

        # 세로 합
        for j in range(5):
            sum_vertical = 0
            for p in range(5):
                sum_vertical += cs[p][j]
            if sum_vertical == 0:
                bingo += 1

        # 대각선합
        cross1 = 0
        for p in range(5):
            cross1 += cs[p][p]
        if cross1 == 0:
            bingo += 1

        # 다른대각선 합
        cross2 = 0
        for p in range(5):
            cross2 += cs[4-p][p]
        if cross2 == 0:
            bingo += 1

        if bingo >= 3:
            print(cnt)
            break
