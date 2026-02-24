# Rの上限が小さいということで、Rに対するbit全探索？
# Cについては、黒が多ければ裏返す。白が多ければそのままとして、
# 多い方の数を合計すれば最適なせんべい数となる

R, C = map(int, input().split())

# Rをbit全探索する時に、せんべいを高速でひっくり返すため、列ごとに煎餅をbitで保持
temp = [list(map(int, input().split())) for _ in range(R)]
columns = [int("".join(map(str, x)), 2) for x in zip(*temp)]

ans = 0
for i in range(1 << R):
    total_count = 0
    for col_val in columns:
        res = col_val ^ i

        count = res.bit_count()
        total_count += max(count, R - count)
    ans = max(ans, total_count)
print(ans)
