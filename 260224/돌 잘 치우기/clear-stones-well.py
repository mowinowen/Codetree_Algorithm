import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())

grid = []
stones = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            stones.append((i, j))
    grid.append(row)
start_points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
ans = 0

def combinations(cnt, idx):
    global ans
    if cnt == m:
        # print(grid)
        visited = [[0] * n for _ in range(n)]
        val = k
        q = deque()
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for sx, sy in start_points:
            visited[sx - 1][sy - 1] = 1
            q.append((sx - 1, sy - 1))
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and not grid[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        val += 1
        
        ans = max(ans, val)
        return
    
    for i in range(idx, len(stones)):
        x, y = stones[i]
        grid[x][y] = 0
        combinations(cnt + 1, i + 1)
        grid[x][y] = 1

combinations(0, 0)
print(ans)