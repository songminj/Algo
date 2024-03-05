import sys

bracket = {'(':')', '[':']' }

while True:
    line = sys.stdin.readline().rstrip()
    stack = []
    if line == '.':
        break
    for l in line:
        if l in bracket.keys(): # 왼쪽 괄호일때
            stack += [l]
        elif l in bracket.values() :  # 오른쪽 괄호일 때
            if stack :
                if l == bracket[stack[-1]]:
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack :
            print('no')
        else:
            print('yes')
