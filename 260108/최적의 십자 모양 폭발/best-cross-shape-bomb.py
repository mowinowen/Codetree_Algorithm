import sys

input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

ans = 0
for i in range(n):
    for j in range(n):
        new_grid = [[-1] * n for _ in range(n)]
        for dx, dy in dirs:
            for num in range(grid[i][j]):
                x = i + dx * num
                y = j + dy * num
                if 0 <= x < n and 0 <= y < n:
                    new_grid[x][y] = 0  
        
        for a in range(n):
            for b in range(n):
                if new_grid[a][b] != 0:
                    new_grid[a][b] = grid[a][b]

        for k in range(n):
            col = []
            for l in range(n):
                if new_grid[l][k] != 0:
                    col.append(new_grid[l][k])
            col = [0] * (n - len(col)) + col

            for l in range(n):
                new_grid[l][k] = col[l]

        cnt = 0
        for k in range(n):
            for l in range(n):
                if new_grid[k][l] != 0:
                    for dx, dy in dirs:
                        if 0 <= k + dx < n and 0 <= l + dy < n and new_grid[k + dx][l + dy] == new_grid[k][l]:
                            cnt += 1
        
        ans = max(ans, cnt)

print(ans // 2)