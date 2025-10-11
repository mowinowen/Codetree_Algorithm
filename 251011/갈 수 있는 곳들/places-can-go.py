from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
q = deque()
# cnt = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 1:
        return False
    
    return True

def bfs():
    global cnt
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
                cnt += 1

ans = 0
for px, py in points:
    if not visited[px - 1][py - 1]:
        cnt = 1
    else:
        cnt = 0
    # cnt = 1
    q.append((px - 1, py - 1))
    visited[px - 1][py - 1] = True
    bfs()
    ans += cnt

print(ans)