# 最小公倍数


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


x, y = map(int, input().split())
print(lcm(x, y))
