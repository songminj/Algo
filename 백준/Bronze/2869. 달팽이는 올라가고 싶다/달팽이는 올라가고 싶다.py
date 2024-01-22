a, b, v = map(int, input().split())

# 마지막날 낮에는 a만큼 오를거라 
# v-b 길이를 a-b씩 몇번 오르는지 확인
# 첫날에 a오른게 v-a보다 큰지 작은지 확인
if (v-b) % (a-b) != 0:
  day = (v-b) // (a-b) + 1
else : 
  day = (v-b) // (a-b) 
print(day)