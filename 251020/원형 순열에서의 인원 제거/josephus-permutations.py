from collections import deque

n, k = map(int, input().split())

# Please write your code here.

d = deque(i for i in range(1, n + 1))

while len(d) != 0:
    for i in range(k - 1):
        front = d.popleft()
        d.append(front)

    print(d[0], end= ' ')
    d.popleft()