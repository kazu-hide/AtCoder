from collections import deque

R, C = map(int, input().split())

sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

# 0 start indexに変換
sy -= 1
sx -= 1
gy -= 1
gx -= 1

grid = [list(input()) for _ in range(R)]

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
distances = [[-1] * C for _ in range(R)]
distances[sy][sx] = 0

q = deque()
q.append((sx, sy))
while q:
    cx, cy = q.popleft()

    for dx, dy in DIRS:
        nx = cx + dx
        ny = cy + dy

        if not (0 <= nx < C and 0 <= ny < R):
            continue
        if grid[ny][nx] == "#":
            continue
        if distances[ny][nx] != -1:
            continue

        distances[ny][nx] = distances[cy][cx] + 1
        q.append((nx, ny))

print(distances[gy][gx])
