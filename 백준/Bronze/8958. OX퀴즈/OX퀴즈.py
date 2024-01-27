test_case = int(input())

# 점수 list
for i in range(test_case):
  result = []
  oxes = list(map(str, input().split()))
  # oxes의 OX를 하나하나 탐색
  for j in range(len(oxes[0])): 
    if oxes[0][j] == 'X': #X이면 0넣기
      result.append(0)

    else :
      result.append(1) # O이면 1넣기
      if j != 0: # 인덱스가 1부터를 탐색하자 
        if oxes[0][j-1] == 'O': # 만약에 앞에 문자도 O이면 
          result[j] = result[j-1] +1 # 앞에 점수값에 +1 한걸 넣자

  print(sum(result))
