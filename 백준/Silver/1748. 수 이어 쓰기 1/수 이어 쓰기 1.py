n = input().strip()
k = len(n)
ans = 0
for i in range(k -1):
    ans += 9 * (10 ** i) * (i+1)
print(ans + (int(n) - 10 ** (k-1) + 1) * k )