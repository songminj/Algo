MM, DD = map(int, input().split())

day31 = [1, 3, 5, 7, 8, 10, 12]
num2day = {1 : 'MON', 2 : 'TUE', 3: 'WED', 4 : 'THU',
       5: 'FRI', 6 : 'SAT', 0 : 'SUN'}

day = DD
if MM > 1:
    for i in range(1, MM):
        if i == 2:
            day += 28
        elif i in day31:
            day += 31
        else:
            day += 30
print(num2day[day%7])