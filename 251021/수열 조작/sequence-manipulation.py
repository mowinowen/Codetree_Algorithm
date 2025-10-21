from collections import deque

n = int(input())

# Please write your code here.
dq = deque([i for i in range(1, n + 1)])

while len(dq) != 1:
    dq.popleft()
    val = dq.popleft()
    dq.append(val)

print(*dq)