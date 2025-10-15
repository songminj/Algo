# 1283번 단축키 지정

import sys
input = sys.stdin.readline

N = int(input())
ans = []
used = set()

for _ in range(N):
    words = input().strip().split()
    chosen = False

    for i, w in enumerate(words):
        if not w:
            continue
        key = w[0].upper()
        if key not in used:
            used.add(key)
            words[i] = f"[{w[0]}]{w[1:]}"
            chosen = True
            break

    if not chosen:
        for i, w in enumerate(words):
            check = False
            for j in range(1, len(w)):
                ch = w[j].upper()
                if ch not in used:
                    used.add(ch)
                    words[i] = w[:j] + f"[{w[j]}]" + w[j + 1:]
                    chosen = True
                    check = True
                    break
            if check:
                break
    ans.append(" ".join(words))
print("\n".join(ans))