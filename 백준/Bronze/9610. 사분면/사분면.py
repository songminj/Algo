import sys
input = sys.stdin.readline
T = int(input())

p = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}

for _ in range(T):
    x, y = map(int, input().split())
    if x ==0 or y == 0:
        p['AXIS'] += 1
    elif x > 0 and y > 0:
        p['Q1'] +=1
    elif x <0 and y > 0:
        p['Q2'] += 1
    elif x < 0and y < 0 :
        p['Q3'] += 1
    elif x > 0 and y < 0 :
        p['Q4'] += 1

for key, item in p.items():
    print(f'{key}: {item}')