import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])
while True:
    if len(cards) == 0:
        break
    print(cards.popleft(), end = ' ')
    cards.rotate(-1)