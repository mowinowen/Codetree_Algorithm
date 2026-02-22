import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0] * m for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()

def can_go(x, y):
    if not(0 <= x < n and 0 <= y < m):
        return False
    
    if visited[x][y] or not a[x][y]:
        return False
    
    return True

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))

visited[0][0] = 1
q.append((0 ,0))
bfs()

if visited[n - 1][m - 1]:
    print(1)

else:
    print(0)