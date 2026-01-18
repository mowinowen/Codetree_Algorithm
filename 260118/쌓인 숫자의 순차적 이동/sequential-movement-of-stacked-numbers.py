import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
pos = {}

for i in range(n):
    row = list(map(int, input().split()))
    for j, num in enumerate(row):
        grid[i][j] = [num]
        pos[num] = (i, j)

move_nums = list(map(int, input().split()))
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for num in move_nums:
    x, y = pos[num]
    max_val = 0
    max_x, max_y = x, y
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]:
            curr_max = max(grid[nx][ny])
            if curr_max > max_val:
                max_val = curr_max
                max_x, max_y = nx, ny

    if (max_x, max_y) == (m, y):
        continue
    
    idx = grid[x][y].index(num)
    grid[max_x][max_y] = grid[x][y][:idx + 1] + grid[max_x][max_y]
    for num in grid[x][y][:idx + 1]:
        pos[num] = (max_x, max_y)
    del grid[x][y][:idx + 1]


for row in grid:
    for cell in row:
        print(*cell) if cell else print('None')