num = int(input())
picks = list(map(int, input().split()))

line = []

for i in range(0, num):
  student_num = i+1
  if picks[i] != 0:
    line.insert(-picks[i], student_num)
  else :
    line.append(student_num)
print(*line)