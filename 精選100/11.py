N, M = map(int, input().split())

masks = []
for _ in range(M):
    mask = 0
    litt = list(map(int, input().split()))[1:]
    for i in litt:
        mask |= 1 << (i - 1)
    masks.append(mask)

p = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    is_light_on = True
    for j in range(M):
        common = (i & masks[j]).bit_count()
        if common % 2 != p[j]:
            is_light_on = False
            break
    if is_light_on:
        ans += 1

print(ans)
