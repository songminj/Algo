import sys

input = sys.stdin.readline

N = int(input())
cost = 0
for _ in range(N):
    time, dd = map(str, input().split())
    hh, mm = time.split(':')
    hh, mm, dd = int(hh), int(mm), int(dd)

    # 초기 시간이 7:00~19:00인지 확인
    if hh >= 7 and hh < 19:
        # 모든 시간이 7:00~19:00사이에 들어온다면
        if hh+(mm+dd) // 60 < 19:
            cost += dd * 10
        # 몇분은 19시전에, 몇분은 19시 이후에
        elif hh + (mm+dd)//60 == 19:
            cost += ((60-mm)*10 + abs(dd-(60-mm))*5)

    elif hh+(mm+dd)//60 == 7:
        cost += ((60-mm)*5 + abs(dd-(60-mm))*10)
    else:
        cost += dd*5

print(cost)
