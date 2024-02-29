import sys

words = list(sys.stdin.readline().strip())
bomb = sys.stdin.readline().strip()
len_words = len(words)
len_bomb = len(bomb)
stack = []
for i in range(len(words)):
    stack.append(str(words[i]))
    if ''.join(stack[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            stack.pop()
else:
    if len(stack) == 0:
        stack = 'FRULA'

print(''.join(stack))