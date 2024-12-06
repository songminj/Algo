# 28464번 Potato

import sys
input = sys.stdin.readline

# 접시개수
N = int(input())
dishes = list(map(int, input().strip().split()))

dishes.sort()

pk = sum(dishes[N//2:])
sw = sum(dishes[:N//2])
print(sw, pk)