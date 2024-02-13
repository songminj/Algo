import sys

test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    vps = sys.stdin.readline().rstrip()
    stack = []
    for string in vps:
        if string == "(":
            stack.append(string)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")

