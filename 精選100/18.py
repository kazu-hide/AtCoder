n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


# Sから２部探索でxを探す
def binary_search(x):
    l, r = 0, n

    while l < r:
        m = (l + r) // 2
        if S[m] == x:
            return m
        elif S[m] > x:
            r = m
        else:
            l = m + 1
    return -1


ans = 0
for t in T:
    idx = binary_search(t)
    if idx != -1:
        ans += 1

print(ans)
