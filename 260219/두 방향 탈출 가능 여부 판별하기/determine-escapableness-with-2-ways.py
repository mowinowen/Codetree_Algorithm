n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(1, 0), (0, 1)]
visited = [[0] * m for _ in range(n)]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    
    if visited[x][y]:
        return False
    
    if not grid[x][y]:
        return False
    
    return True

def dfs(x, y):
    visited[x][y] = 1
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)
print(visited[n-1][m-1])