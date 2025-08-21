import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
known = list(map(int, input().strip().split()))

parties = []
for _ in range(M):
    line = list(map(int, input().split()))
    k, *people = line
    parties.append(set(people))

def spread_truth(initial: set) -> set:
    S = set(initial)
    changed = True
    while changed:
        changed = False
        for p in parties:
            if p & S:
                before = len(S)
                S |= p
                if len(S) > before:
                    changed = True
    return S

def count_lie_parties(truth_people: set) -> int:
    ans = 0
    for p in parties:
        if not (p & truth_people):
            ans += 1
    return ans

if known[0] == 0:
    print(M)
else:
    _, *initial = known
    all_truth = spread_truth(set(initial))
    print(count_lie_parties(all_truth))