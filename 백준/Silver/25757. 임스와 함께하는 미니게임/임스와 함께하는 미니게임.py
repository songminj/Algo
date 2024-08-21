# 25757번 임스와 함께하는 미니게임

import sys
input = sys.stdin.readline

N, game = input().strip().split()

# 전처리
N = int(N)
if game == 'Y':
    game = 1
elif game == 'F':
    game = 2
else :
    game = 3

players = set()
for _ in range(N):
    name = input()
    players.add(name)

print(len(players)// game)