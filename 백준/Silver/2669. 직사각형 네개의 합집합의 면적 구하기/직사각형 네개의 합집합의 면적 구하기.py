area_set = set()
# 좌표값을 set함수에 넣는다 
for i in range(4):
  x1, y1, x2, y2 = map(int, input().split())
  for p in range(x1, x2):
    for q in range(y1, y2):
      cell = (p, q)
      area_set.add(cell)

print(len(area_set))