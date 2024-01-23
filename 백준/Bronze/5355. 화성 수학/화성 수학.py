test_case = int(input())

for case in range(test_case):
  num, *operators = map(str, input().split())
  num = float(num)
  for operator in operators:
    if operator == '@':
      num *= 3
    elif operator == '%':
      num += 5
    else :
      num -= 7
  print('%0.2f'%num)