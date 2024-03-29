import sys
input = sys.stdin.readline

n = int(input())
order = [int(input()) for _ in range(n)]
idx = 1
res = []
def cal_stack(stack):
    global res, idx
    for num in order:
        if stack[-1] < num:
            if idx < num +1:
                for i in range(idx, num + 1):
                    stack.append(i)
                    res.append('+')
                stack.pop()
                res.append('-')
                idx = num+1
            else:
                return 'NO'
        elif stack[-1] > num:
            for _ in range(len(stack)+1):
                tmp = stack.pop()
                res.append('-')
                if tmp == num:
                    break
            else:
                return 'NO'
        elif stack[-1] == num:
            stack.pop()
            res.append('-')
    return '\n'.join(res)


print(cal_stack([0]))