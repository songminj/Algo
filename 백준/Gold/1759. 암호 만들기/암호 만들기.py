import sys

n, c = map(int, sys.stdin.readline().strip().split())
words = sorted(list(sys.stdin.readline().strip().split()))

def make_code(k, words, res, flag, con):

    if len(res) == n and flag and con >= 2:
        print(''.join(res))
        return

    for i in range(k, c):
        res.append(words[i])
        k = i + 1
        if words[i] in 'aeiou' and not flag:
            flag = True
            make_code(k, words, res, flag, con)
            flag = False
        elif words[i] not in 'aeiou':
            make_code(k, words, res, flag, con+1)
        else:
            make_code(k, words, res, flag, con)
        res.pop()


make_code(0, words, [], False, 0)
