def solution(wallpaper):
    r, c = len(wallpaper), len(wallpaper[0])
    answer = [r, c, 0, 0]
    for i in range(r):
        for j in range(c):
            if wallpaper[i][j] == '#':
                if answer[0] > i:
                    answer[0] = i
                if answer[1] > j:
                    answer[1] = j
                if answer[2] < i:
                    answer[2] = i
                if answer[3] < j:
                    answer[3] = j
    answer[2], answer[3] = answer[2]+1, answer[3]+1
    return answer