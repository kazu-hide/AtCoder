N, M = map(int, input().split())

# relations[i]は議員 i と知り合いである議員の集合のビット
relations = [0] * N

for i in range(N):
    relations[i] |= 1 << i


for _ in range(M):
    x, y = map(int, input().split())
    relations[x - 1] |= 1 << y - 1
    relations[y - 1] |= 1 << x - 1


# 派閥に参加している議員をbit で表し、組み合わせを全探索する
max_size = 0
for i in range(1 << N):
    size = i.bit_count()
    is_valid = True
    for j in range(N):
        # もし議員jが派閥iに含まれているなら
        if (i >> j) & 1:
            # 議員jの知り合い relations[j]に派閥i が全て含まれるかチェック
            if (relations[j] & i) != i:
                is_valid = False
                break

    if is_valid:
        max_size = max(max_size, size)
print(max_size)
