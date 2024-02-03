# N : 총 학생수 K : 한방에 배정할 수 있는 최대인원수 
N, K = map(int, input().split())
# 조건에 맞으면 한명씩 +1 준다 
now = [[0, 0] for _ in range(7)]  # 방
cnt = 0

# (S, Y) : 성별, 나이 가 주어진다
for _ in range(N):
  s, y = map(int, input().split())
  now[y][s] += 1

for i in range(2):
  for j in range(1, 7):
    cnt += now[j][i] // K
    if (now[j][i] % K) != 0:
      cnt += 1 
print(cnt)