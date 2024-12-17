# 23443번 Javascript

import sys
input = sys.stdin.readline

x, y = input().strip().split()

def cal(x, y):
    try:
        num_x = float(x)
        num_y = float(y)
        print(int(num_x - num_y))
    except ValueError:
        print("NaN")
cal(x, y)