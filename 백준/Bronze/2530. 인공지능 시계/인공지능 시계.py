h, m, s = map(int, input().split())
d = int(input())

total = s + m*60 + h*60*60 + d
real_m = (total // 60) % 60
real_h = (total // 60) // 60
real_s = total % 60

if real_h >= 24:
  real_h = real_h % 24

print(f'{real_h} {real_m} {real_s}')