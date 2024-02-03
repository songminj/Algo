lst = list()
# 9명 키 받기 
for _ in range(9):
  a = int(input())
  lst = lst + [a]

# 비트 연산으로 

for i in range(1<<9):
    if bin(i).count('1') == 7:
        sum_set = 0
        result = []
        for j in range(9):
            if i & (1<< j):
                sum_set += lst[j]
                result.append(lst[j])
        if sum_set == 100:
            result.sort()
            print(*result, sep='\n')
            break