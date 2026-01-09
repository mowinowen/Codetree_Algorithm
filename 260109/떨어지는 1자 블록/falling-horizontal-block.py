import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
isbool = True
for i in range(n):
    for j in range(m):
        if grid[i][k - 1 + j] == 1:
            isbool = False
            r = i - 1
            break
        
    if not isbool:
        break

if isbool:
    r = n - 1

for i in range(m):
    grid[r][k - 1 + i] = 1

for row in grid:
    print(*row)