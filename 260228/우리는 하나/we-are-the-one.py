import sys
from collections import deque
input = sys.stdin.readline

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = []
all_pos = [(i, j) for i in range(n) for j in range(n)]
max_ans = 0
def dfs(cnt, idx):
    global max_ans
    if cnt == k:
        visited = [[0] * n for _ in range(n)]
        ans = k
        q = deque()
        for x, y in result:
            visited[x][y] = 1
            q.append((x, y))

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if u <= abs(grid[x][y] - grid[nx][ny]) <= d:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        ans += 1
        max_ans = max(ans, max_ans)
        return
    
    for i in range(idx, n * n):
        result.append(all_pos[i])
        dfs(cnt + 1, i + 1)
        result.pop()

dfs(0, 0)
print(max_ans)