# 1546. 평균 

#과목 개수를 받는다
n = int(input())

# 현재 성적을 받는다
result = list(map(int, input().split()))

result.sort(reverse =True)
high = result[0]

left = sum(result)

new_average = ((left / high ) * 100) / n
print('%0.9f'%new_average) 