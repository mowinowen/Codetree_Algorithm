n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n - 1):
    for j in range(m - 1):
        box = [grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]
        ans = max(sum(box) - min(box), ans)

for row in grid + list(zip(*grid)):
    for i in range(len(row) - 2):
        ans = max(ans, sum(row[i : i + 3]))

print(ans)