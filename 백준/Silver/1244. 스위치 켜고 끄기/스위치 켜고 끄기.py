# 1244번 스위치 켜고 끄기

'''
남학생
스위치 번호 = 자기번호 * k 이면 스위치 상태 바꿈

여학생
자기번호 기준 좌우 대칭으로
가장 많은 스위치를 포함하는 구간을 찾아서
그 구간에 속한 스위차 상태 변경
'''

import sys
input = sys.stdin.readline

def man(k, arr):
    for i in range(k-1, N, k):
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr

def woman(k, arr):
    k -= 1
    if arr[k]:
        arr[k] = 0
    else:
        arr[k] = 1
    for i in range(1, N//2):
        if k+i >= N or k-i < 0:
            break
        if arr[k+i] == arr[k-i]:
            if arr[k+i]:
                arr[k+i], arr[k-i] = 0, 0
            else:
                arr[k+i], arr[k-i] = 1, 1
        else:
            break
    return arr

N = int(input())
switch = list(map(int, input().strip().split()))
T = int(input())
for _ in range(T):
    s, num = map(int, input().strip().split())
    if s == 1:
        switch = man(num, switch)
    else:
        switch = woman(num, switch)

for i in range(0, N, 20):
    print(*switch[i:i+20])