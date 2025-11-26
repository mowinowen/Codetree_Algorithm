n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n - 1):
    for j in range(m - 1):
        min_num = float('inf')
        sum_num = 0
        for a in range(i, i + 2):
            for b in range(j, j + 2):
                min_num = min(min_num, grid[a][b])
                sum_num += grid[a][b]
        ans = max(sum_num - min_num, ans)

for row in grid + list(zip(*grid)):
    sum_num = sum(row[:3])
    ans = max(sum_num, ans)
    if len(row) > 3:
        for i in range(3, len(row)):
            sum_num = sum_num - row[i - 3] + row[i]
            ans = max(sum_num, ans)

print(ans)