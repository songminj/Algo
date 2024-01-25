# 11728 배열 합치기 Silver 5

a, b = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.extend(b_list)
a_list.sort()
print(*a_list)