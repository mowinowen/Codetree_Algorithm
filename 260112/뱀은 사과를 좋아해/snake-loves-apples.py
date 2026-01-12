import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
apples = [tuple(map(int, input().split())) for _ in range(M)]
moves = [input().strip().split() for _ in range(K)]

grid = [[0] * N for _ in range(N)]
for x, y in apples:
    grid[x - 1][y - 1] = 1

dirs = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}
x, y = 0, 0
curr_len = 1
ans = 0
isend = False
dq = deque((x, y))

for d, num in moves:
    num = int(num)
    dx, dy = dirs[d]

    for _ in range(num):
        if not (0 <= x + dx < N and 0 <= y + dy < N):
            ans += 1
            isend = True
            break

        if (x + dx, y + dy) in dq:
            ans += 1
            isend = True
            break
        
        if grid[x + dx][y + dy] == 1:
            grid[x + dx][y + dy] = 0
            dq.append((x + dx, y + dy))
        
        else:
            dq.append((x + dx, y + dy))
            dq.popleft()

        x, y = x + dx, y + dy
        ans += 1

    
    if isend:
        break

print(ans)

# Please write your code here.