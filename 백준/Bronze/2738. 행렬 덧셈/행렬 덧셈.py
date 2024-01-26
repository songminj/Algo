n, m = map(int, input().split())
a_list = []
b_list = []
result_list = []

for i in range(n):
  a_arr = list(map(int, input().split()))
  a_list.append(a_arr)

for i in range(n):
  b_arr = list(map(int, input().split()))
  b_list.append(b_arr)

for i in range(n):
  result_arr = []
  for j in range(m):
    result_cell = str(a_list[i][j]+b_list[i][j])
    result_arr.append(result_cell)
  result_list.append(result_arr)

for arr in result_list:
  print(' '.join(arr))