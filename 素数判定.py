# 素数判定


def get_prime_numbers(x):
    if x < 2:
        return []

    is_prime = [True] * (x + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(x**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, x + 1, p):
                is_prime[i] = False

    return [p for p in range(2, x + 1) if is_prime[p]]


x = int(input())
print(get_prime_numbers(x))
