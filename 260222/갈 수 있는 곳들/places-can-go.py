import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_pos = [tuple(map(int, input().split())) for _ in range(m)]

visited = [[0] * n for _ in range(n)]
q = deque()
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    if visited[x][y] or grid[x][y]:
        return False
    
    return True

def bfs():
    global ans
    while q:
        x, y = q.popleft()
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = 1
                ans += 1
                q.append((nx, ny))

ans = 0
for x, y in start_pos:
    q.append((x - 1, y - 1))
    if not visited[x - 1][y - 1]:
        visited[x - 1][y - 1] = 1
        ans += 1
    bfs()

print(ans)