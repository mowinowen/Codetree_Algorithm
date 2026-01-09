import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
for i in range(1, n):
    isbool = True
    for j in range(m):
        if grid[i][k - 1 + j] == 1:
            isbool = False
            break
        
    if not isbool:
        for j in range(m):
            grid[i - 1][k - 1 + j] = 1
        break

for row in grid:
    print(*row)