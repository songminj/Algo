import sys
input = sys.stdin.readline


def triangle(a, b, c):
    if c < a+ b:
        if a == b and b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'Invalid'


while True:
    lines = list(map(int, input().split()))
    lines.sort()
    if sum(lines) > 0:
        print(triangle(lines[0], lines[1], lines[2]))
    else:
        break