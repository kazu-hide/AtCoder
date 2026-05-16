import heapq

X = int(input())
Q = int(input())

# 2つのheapqで中央値を常に求める
# left, rightのqueueを用意し、rightの最小値が中央値であるようにする
left = []
right = [X]
heapq.heapify(left)
heapq.heapify(right)

ans = []
for _ in range(Q):
    A, B = map(int, input().split())

    curr_median = right[0]
    if A <= curr_median:
        # leftは最大値heapにする
        heapq.heappush(left, A * -1)
    else:
        heapq.heappush(right, A)

    if B <= curr_median:
        # leftは最大値heapにする
        heapq.heappush(left, B * -1)
    else:
        heapq.heappush(right, B)

    while len(left) + 1 > len(right):
        top = heapq.heappop(left) * -1
        heapq.heappush(right, top)

    while len(left) + 1 < len(right):
        top = heapq.heappop(right)
        heapq.heappush(left, top * -1)

    ans.append(right[0])

for a in ans:
    print(a)
