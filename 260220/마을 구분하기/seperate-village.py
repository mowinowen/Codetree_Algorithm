import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0] * n for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    if not grid[x][y]:
        return False
    
    if visited[x][y]:
        return False
    
    return True

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        
        if can_go(nx, ny):
            dfs(nx, ny)

l = []
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            l.append(cnt)

print(len(l))
l.sort()
for num in l:
    print(num)