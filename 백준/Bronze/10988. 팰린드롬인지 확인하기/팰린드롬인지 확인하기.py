import sys
input = sys.stdin.readline

pel = input().strip()
reverse = pel[::-1]
if pel == reverse:
    print(1)
else:
    print(0)