def solution(storey):
    answer = 0
    
    while storey > 0:
        # 현재 일의 자리 숫자와 그 다음 자릿수 숫자 확인
        current_digit = storey % 10
        next_digit = (storey // 10) % 10
        
        # 1. 현재 숫자가 5보다 큰 경우 -> 올림
        if current_digit > 5:
            answer += (10 - current_digit)
            storey = (storey // 10) + 1
            
        # 2. 현재 숫자가 5인 경우 -> 다음 숫자를 보고 결정
        elif current_digit == 5:
            # 다음 숫자가 5 이상이면 올림이 이득
            if next_digit >= 5:
                answer += (10 - current_digit)
                storey = (storey // 10) + 1
            # 다음 숫자가 5 미만이면 내림이 이득
            else:
                answer += current_digit
                storey //= 10
                
        # 3. 현재 숫자가 5보다 작은 경우 -> 내림
        else:
            answer += current_digit
            storey //= 10
            
    return answer