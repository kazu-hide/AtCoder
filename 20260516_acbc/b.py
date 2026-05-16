H, W = map(int, input().split())

Grid = [[4] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            Grid[i][j] -= 1
        if i == H - 1:
            Grid[i][j] -= 1
        if j == 0:
            Grid[i][j] -= 1
        if j == W - 1:
            Grid[i][j] -= 1

for i in range(H):
    print(*Grid[i])
