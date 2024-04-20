import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
iscard = list(map(int, input().split()))

def list2dict(numbers):
    result_dict = {}
    for number in numbers:
        result_dict[number] = 0
    return result_dict

card_dic = list2dict(iscard)

for c in cards:
    if c in card_dic.keys():
        card_dic[c] += 1
print(*card_dic.values())
