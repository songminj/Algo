import sys

# 듣도못한, 보도못한
listen, see = map(int, sys.stdin.readline().split())
listen_set = set()
see_set = set()
# print(listen, see)
for i in range(listen):
    listen_set.add(sys.stdin.readline().strip())
for i in range(see):
    see_set.add(sys.stdin.readline().strip())

inter = sorted(list(listen_set & see_set))
print(len(inter))
print('\n'.join(inter))