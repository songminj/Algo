# num : 카드의 개수, card_sum : 카드의 합
num, card_sum = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(num-2):
  for j in range(i+1, num-1):
    for k in range(j+1, num):
      target = cards[i] + cards[j] + cards[k]
      if max_sum < target <= card_sum :
        max_sum = target

print(max_sum)