n = int(input())
grid = [[0] * (n + 1)]+[[0] + list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for dx, dy in dirs:
    for i in range(1, grid[r][c]):
        if 1 <= r + dx * i <= n and 1 <= c + dy * i <= n:
            grid[r + dx * i][c + dy * i] = 0

grid[r][c] = 0

for i in range(1, n + 1):
    temp = [grid[j][i] for j in range(1, n + 1) if grid[j][i] != 0]
    temp = [0] * (n - len(temp)) + temp
    for j in range(1, n + 1):
        grid[j][i] = temp[j - 1]

for row in grid[1:]:
    print(*row[1:])