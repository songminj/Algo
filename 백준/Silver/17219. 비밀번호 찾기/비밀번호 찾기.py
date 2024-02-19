site, find = map(int, input().split())
dic = {}

for i in range(site):
    key, pw = map(str, input().split())
    dic[key] = pw

for i in range(find):
    missing = input()
    print(dic[missing])