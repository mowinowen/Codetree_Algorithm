n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
gold_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

ans = 0
for i in range(n):
    for j in range(n):
        dists = sorted([abs(x - i) + abs(y - j) for x, y in gold_pos])
        for idx, k in enumerate(dists):
            if k ** 2 + (k + 1) ** 2 <= (idx + 1) * m:
                ans = max(ans, idx + 1)

print(ans)