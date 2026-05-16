S = input()

n = len(S)

count = 0
for i in range(n):
    if S[i] == "C":
        count += min(i, n - i - 1)
        # 自分自身を追加
        count += 1
print(count)
