total = 0
for _ in range(5):
    point = int(input())
    if point < 40:
        total += 40
    else:
        total += point
print(total // 5)