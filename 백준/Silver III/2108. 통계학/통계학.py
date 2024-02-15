
import sys
n= int(sys.stdin.readline())
dic_num = {}
list_num = []
for _ in range(n):
    num = int(sys.stdin.readline())
    # 딕셔너리에 해당 키가 존재하지 않으면 0으로 초기화 후 1 증가
    dic_num[num] = dic_num.get(num, 0) + 1
    list_num.append(num)

list_num.sort()
# 산술평균
avg = sum(list_num)/n
if avg >= 0:
    if avg % 1 >= 0.5:
        print(int(avg)+1)
    else:
        print(int(avg))
else:
    if abs(avg) % 1 >= 0.5:
        print(int(avg)-1)
    else:
        print(int(avg))

# 중앙값
print(list_num[n//2])
# 최빈값
freq = [k for k, v in dic_num.items() if max(dic_num.values()) == v]
freq.sort()
if len(freq) > 1:
    print(freq[1])
else:
    print(freq[0])

# 범위
print(abs(list_num[-1]-list_num[0]))
