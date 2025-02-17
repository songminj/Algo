def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for idx in range(n):
        h, m = schedules[idx] // 100, schedules[idx] % 100 + 10
        if m >= 60:
            h += 1
            m -= 60
        flag = True
        for i in range(7):
            today = (i+startday) % 7
            if (today == 6) or (today == 0):
                continue
            nh, nm = timelogs[idx][i] // 100, timelogs[idx][i] % 100
            if nh < h:
                continue
            elif (nh == h) & (nm <= m):
                continue
            else:
                flag = False
                break
        if flag:
            answer += 1
    return answer