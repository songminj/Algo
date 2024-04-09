def solution(clothes):
    dic = {}
    for cloth in clothes:
        name, cloth_type = cloth
        dic[cloth_type] = dic.get(cloth_type, []) + [name]
    answer = 1
    for key in dic.keys():
        answer *= (len(dic[key]) +1)
    return answer -1