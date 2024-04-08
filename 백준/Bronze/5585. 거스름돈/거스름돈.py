import sys

input = sys.stdin.readline

exchange = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}
n = int(input())
n = 1000-n
for money in exchange.keys():
    while True:
        if n < money:
            break
        n -= money
        exchange[money] += 1
print(sum(exchange.values()))