import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def can_go(x, y, val):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] >= val:
        return False
    return True

def bfs(val):
    global new_value, start_x, start_y
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny, val):
                visited[nx][ny] = 1
                q.append((nx, ny))

                if (new_value, -start_x, -start_y) < (grid[nx][ny], -nx, -ny):
                    new_value, start_x, start_y = grid[nx][ny], nx, ny
    
    return start_x + 1, start_y + 1

for _ in range(k):
    visited = [[0] * n for _ in range(n)]
    q = deque()  

    start_x, start_y = r - 1, c - 1
    new_value = 0

    q.append((r - 1, c - 1))
    visited[r - 1][c - 1] = 1
    r, c = bfs(grid[r - 1][c - 1])

print(r, c)