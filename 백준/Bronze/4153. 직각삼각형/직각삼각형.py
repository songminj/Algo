while True:
  triangle = list(map(int, input().split()))
  #탈출 조건 
  if sum(triangle) == 0:
    break 

  triangle.sort()
  if triangle[2] ** 2 == triangle[0] **2 + triangle[1]**2:
    print('right')
  else:
    print('wrong') 