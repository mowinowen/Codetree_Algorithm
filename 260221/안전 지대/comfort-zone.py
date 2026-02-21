import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_num = 1
for row in grid:
    max_num = max(max(row), max_num)

def can_go(x, y, k):
    if not (0 <= x < n and 0 <= y < m):
        return False
    
    if visited[x][y]:
        return False
    
    if grid[x][y] <= k:
        return False
    
    return True

def dfs(x, y):
    visited[x][y] = 1
    
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        
        if can_go(nx, ny, k):
            dfs(nx, ny)

max_ans = 0
max_k = 1
for k in range(1, max_num + 1):
    ans = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (not visited[i][j]) and (grid[i][j] > k):
                dfs(i, j)
                ans += 1
    if max_ans < ans:
        max_ans = ans
        max_k = k

print(max_k, max_ans)