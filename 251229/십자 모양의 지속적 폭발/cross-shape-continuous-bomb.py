import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(m):
    c = int(input())
    for i in range(n):
        if grid[i][c - 1]:
            val = grid[i][c - 1]

            grid[i][c - 1] = 0
            for v in range(val):
                for dx, dy in dirs:
                    if 0 <= c - 1 + dy * v < n and 0 <= i + dx * v < n:
                        grid[i + dx * v][c - 1 + dy * v] = 0
            break

    else:
        continue
    
    new_grid = []
    for col in zip(*grid):
        new_col = [c for c in col if c]
        new_col = [0] * (n - len(new_col)) + new_col
        new_grid.append(new_col)
    
    grid = list(map(list, zip(*new_grid)))

for row in grid:
    print(*row)