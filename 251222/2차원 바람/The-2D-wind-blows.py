import sys
input = sys.stdin.readline
from collections import deque

n, m, q = map(int, input().split())

# Create 2D array for building state
a = [[-1] * m] + [[-1] + list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

def in_range(x, y):
    return 0 < x < n + 1 and 0 < y < m + 1

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for r1, c1, r2, c2 in winds:
    lengths = [c2 - c1, r2 - r1, c2 - c1, r2 - r1]
    positions, vals = [], deque()

    for (dx, dy), l in zip(dirs, lengths):
        for _ in range(l):
            r1 += dx
            c1 += dy
            positions.append((r1, c1))
            vals.append(a[r1][c1])
    
    vals.rotate(1)

    for (x, y), val in zip(positions, vals):
        a[x][y] = val

    update_val = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if r1 <= i <= r2 and c1 <= j <= c2:
                sum_val = a[i][j]
                cnt = 1

                for dx, dy in dirs:
                    if in_range(i + dx, j + dy):
                        sum_val += a[i + dx][j + dy]
                        cnt += 1
                update_val[(i, j)] = sum_val // cnt

    for (i, j), sum_val in update_val.items():
        a[i][j] = sum_val

for row in a[1:]:
    print(*row[1:])
