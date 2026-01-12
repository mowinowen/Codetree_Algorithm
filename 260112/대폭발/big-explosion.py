import sys
input = sys.stdin.readline

n, m, r, c = map(int, input().split())

# Please write your code here.

grid = [[-1] * n for _ in range(n)]
grid[r - 1][c - 1] = 0
ans = 1
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(1, m + 1):
    for x in range(n):
        for y in range(n):
            if grid[x][y] != -1 and grid[x][y] != i:
                for dx, dy in dirs:
                    nx = x + dx * (2 ** (i - 1))
                    ny = y + dy * (2 ** (i - 1))
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == -1:
                        grid[nx][ny] = i
                        ans += 1

print(ans)