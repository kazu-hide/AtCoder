import math
from itertools import permutations

N = int(input())
towns = []

for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

perms = list(permutations(range(N), N))

dist = 0
for p in perms:
    for i in range(1, len(p)):
        dist += math.sqrt(
            (towns[p[i]][0] - towns[p[i - 1]][0]) ** 2
            + (towns[p[i]][1] - towns[p[i - 1]][1]) ** 2
        )

print(dist / len(perms))
