num = int(input())
num_list = []
result = []

for i in range(1, num+1):
  # 1, 2번째 수까지 만들어주기 
  num_list.append(num)
  num_list.append(i)

  # 뒷자리 수도 쭉 ~ 만들어주기 
  j = 0
  while True :
    new = num_list[j] - num_list[j+1]
    # new가 0 보다 작을때 탈출
    if new < 0:
      break
    j += 1 
    num_list.append(new)

  # result보다 숫자가 많이 만들어지면 result 값을 바꿔준다.
  if len(result) < len(num_list):
    result = num_list.copy()
  
  num_list.clear()

print(len(result))
print(*result)