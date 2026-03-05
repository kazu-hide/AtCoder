from collections import deque


def count_islands(w, h):

    grid = [list(input().split()) for _ in range(h)]

    DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    visited = [[False] * w for _ in range(h)]

    countOfIslands = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] != "1":
                continue

            if visited[r][c]:
                continue

            countOfIslands += 1

            q = deque()
            q.append((c, r))
            while q:
                cc, cr = q.pop()
                for dr, dc in DIRS:
                    nr = cr + dr
                    nc = cc + dc
                    if not (0 <= nr < h and 0 <= nc < w):
                        continue
                    if grid[nr][nc] != "1":
                        continue
                    if visited[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    q.append((nc, nr))

    return countOfIslands


ans = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ans.append(count_islands(w, h))

for a in ans:
    print(a)
