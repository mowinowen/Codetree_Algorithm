import sys
input = sys.stdin.readline

n = int(input())
grid = []
max_num = 0
for _ in range(n):
    row = list(map(int, input().split()))
    max_num = max(max_num, max(row))
    grid.append(row)

visited = [[0] * n for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def can_go(x, y, k):
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    if visited[x][y]:
        return False
    
    if grid[x][y] == k:
        return True
    
    return False
    
def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny)

bomb_block, max_block = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            k = grid[i][j]
            cnt = 0
            dfs(i, j)

            if cnt >= 4:
                bomb_block += 1
            max_block = max(max_block, cnt)

print(bomb_block, max_block)