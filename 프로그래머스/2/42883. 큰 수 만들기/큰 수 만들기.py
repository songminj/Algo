def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -=1
        stack.append(num)
    if k > 0:
        return ''.join(stack[:-k])
    else: 
        return ''.join(stack)