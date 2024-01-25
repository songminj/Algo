# 2839 설탕 

sugar = int(input())
sugar_3 = 0
# 일단 5kg 봉투에 다 넣음 
sugar_5, remain = divmod(sugar, 5)

# 나머지 개수에 따라서 3kg 봉투 개수를 계산
if remain % 3 == 0 : 
  sugar_3 = remain // 3
elif remain % 3 == 1 :
    if sugar_5 >= 1:
       sugar_5 -= 1
       sugar_3 = (remain + 5) // 3
    else : # 만약에 5kg 가 안되면 
       sugar_3 =-1
else :
    if sugar_5 >= 2:
       sugar_5 -= 2
       sugar_3 = (remain + 10) // 3
    else :
       sugar_5 = 0
       sugar_3 = -1  


print(sugar_3+sugar_5)