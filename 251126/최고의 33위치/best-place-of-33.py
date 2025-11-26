n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n - 2):
    for j in range(n - 2):
        cnt = sum(grid[a][b] == 1 for a in range(i, i + 3) for b in range(j, j + 3))
        ans = max(ans, cnt)

print(ans)  