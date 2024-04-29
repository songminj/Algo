import sys
input = sys.stdin.readline

from heapq import heappush, heappop, heapify

N, M = map(int, input().split())
cards = list(map(int, input().split()))
heapify(cards)
for _ in range(M):
    x, y = heappop(cards), heappop(cards)
    new = x+y
    heappush(cards, new)
    heappush(cards, new)
print(sum(cards))