n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            sum_val = 0
            for x in range(n):
                for y in range(n):
                    if abs(i - x) + abs(j - y) <= k and grid[x][y]:
                        sum_val += 1
            if k ** 2 + (k + 1) ** 2 <= sum_val * m:
                ans = max(ans, sum_val)

print(ans)