n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(1, 0), (0, 1)]
visited = [[0] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = 1
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if (0 <= nx < n) and (0 <= ny < m) and (not visited[nx][ny]) and grid[nx][ny]:
            dfs(nx, ny)

dfs(0, 0)

if visited[n - 1][n - 1]:
    print(1)
else:
    print(0)