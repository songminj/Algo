
# 최대공약수
def gcd(a, b):
    while b > 0 :
        a, b = b, a % b
    return a

# 최소공배수
def lcd(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcd(a, b))