# 총 라운드 수
round = int(input())

# 라운드 (a가 낸 개수, 그림 ) (b가 낸 개수, 그림) 
# 별 : 4, 동그라미 : 3, 네모 :2 , 세모 :1

for _ in range(round):
    a_count, *a_card = map(int, input().split())
    b_count, *b_card = map(int, input().split())
    a_card.sort()
    b_card.sort() 
    if a_card == b_card :
        print("D")

    for i in range(4, 0, -1):
        if a_card.count(i) > b_card.count(i):
            print("A")
            break
        elif a_card.count(i) < b_card.count(i):
            print("B")
            break
        else :
            continue