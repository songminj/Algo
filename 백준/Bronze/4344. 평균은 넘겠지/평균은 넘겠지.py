# 4344. 평균은 넘겠지 Bronze1

# 테스트 케이스 받기
test_case = int(input())

for i in range(test_case):
  # student 와 점수결과 변수 받기
  student, *result = list(map(int, input().split()))
  avg = sum(result)/student
  cnt = 0 
  
  # 평균을 넘는 학생 수 세기
  for j in range(student):
    if result[j] > avg:
      cnt += 1
  
  upper = (cnt / student) *100
  print('%0.3f'%round(upper, 3)+'%')