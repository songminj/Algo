sound = list(map(int, input().split()))
diff_sound = []

for i in range(7):
  diff_sound.append(sound[i]-sound[i+1])

if diff_sound == [-1, -1, -1, -1, -1, -1, -1]:
  print('ascending')
elif diff_sound == [1, 1, 1, 1, 1, 1, 1] :
  print('descending')
else:
  print('mixed')