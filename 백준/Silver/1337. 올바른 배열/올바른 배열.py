import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))
arr.sort()
ans = 5
for i in range(N):
    cnt1=4
    cnt2=4
    for j in range(N):
        if arr[i]+5>arr[j] and arr[i]<arr[j]:
            cnt1-=1
        elif arr[i]-5<arr[j] and arr[i]>arr[j]:
            cnt2-=1
    ans = min(ans, cnt1, cnt2)
    
print(ans)