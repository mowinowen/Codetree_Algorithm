import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
isbool = True
r = n - 1
for i in range(n):
    if 1 in grid[i][k - 1 : k + m - 1]:
        r = i - 1
        break

grid[r][k - 1 : k + m - 1] = [1] * m

for row in grid:
    print(*row)