# BOJ 3052. 나머지 
mods = set()
for i in range(10):
    mod = (int(input())) % 42
    mods.add(mod)
print(len(mods))