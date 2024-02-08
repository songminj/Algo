# N: 개수 
n = int(input())

# n개의 정수 
n_set = set(input().split())
m = int(input())
m_set = input().split()

for num in m_set:
  if num in n_set:
    print(1)
  else:
    print(0)