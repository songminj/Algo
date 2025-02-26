from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2) 
    target = (sum1 + sum2) // 2
    
    # 합이 홀수라면 나눌 수 없음
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    total_len = len(q1) + len(q2)
    count = 0
    left, right = 0, len(q1)  # 투 포인터

    # 두 큐를 하나로 연결된 리스트처럼 관리
    queue = q1 + q2
    
    while left < total_len and right < total_len:
        if sum1 == target:
            return count  # 최소 연산 횟수 반환
        
        if sum1 < target and right < total_len:
            sum1 += queue[right]  # 오른쪽 값 추가
            right += 1
        else:
            sum1 -= queue[left]  # 왼쪽 값 제거
            left += 1
        
        count += 1
    
    return -1  # 만들 수 없는 경우
