import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))
LIS = [arr[0]]

def find(n):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start+end) //2
        if LIS[mid] == n:
            return mid
        elif LIS[mid] < n:
            start = mid+1
        else:
            end = mid-1
    return start

for num in arr:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        idx = find(num)
        LIS[idx] = num

print(len(LIS))