# n과 m (11)

n, m = map(int, input().split())
digits = list(map(int, input().split()))
digits.sort()


def perm(m, lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    before = 0
    for i in range(n):
        if before != digits[i]:
            before = digits[i]
            perm(m, lst + [str(digits[i])])


perm(m, [])
