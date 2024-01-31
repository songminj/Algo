N = int(input()) # 로프의 개수
lst = []

for i in range(N):
  lst.append(int(input()))
  
lst.sort(reverse=True)

max_weight = lst[0]
for i in range(1, N):
  weight = lst[i] * (i+1)

  if weight > max_weight:
    max_weight = weight

print(max_weight)