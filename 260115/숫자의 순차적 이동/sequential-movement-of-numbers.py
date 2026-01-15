import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for _ in range(m):
    num_and_pos = sorted([(grid[i][j], i, j) for i in range(n) for j in range(n)])

    for num, x, y in num_and_pos:
        max_val = 0
        for dx, dy in dirs:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if grid[x + dx][y + dy] > max_val:
                    max_val = grid[x + dx][y + dy]
                    nx, ny = x + dx, y + dy
        
        num_and_pos[grid[nx][ny] - 1] = (grid[nx][ny], x, y)
        grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]

for row in grid:
    print(*row)