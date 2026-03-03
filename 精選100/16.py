from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
perms = list(permutations(range(1, N + 1), N))

p_idx = -1
q_idx = -1
for i in range(len(perms)):
    if perms[i] == P:
        p_idx = i
    if perms[i] == Q:
        q_idx = i

print(abs(p_idx - q_idx))
