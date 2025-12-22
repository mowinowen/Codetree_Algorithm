from collections import deque

n = int(input())
grid = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

d = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
lengths = [m1, m2, m3, m4]
positions, vals = [], deque()

for (dx, dy), m in zip(d, lengths):
    for _ in range(m):
        r += dx
        c += dy
        positions.append((r, c))
        vals.append(grid[r][c])

if dir == 0:
    vals.rotate(1)

else:
    vals.rotate(-1)
    
for (x, y), val in zip(positions, vals):
    grid[x][y] = val

for row in grid[1:]:
    print(*row[1:])