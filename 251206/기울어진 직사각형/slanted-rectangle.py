n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def sum_value(r, c, x, y):
    sum_val = 0
    d = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

    for i in range(4):
        m = r if i % 2 == 0 else c
        for _ in range(1, m + 1):
            if in_range(x + d[i][0], y + d[i][1]):
                x, y = x + d[i][0], y + d[i][1]
                sum_val += grid[x][y]
            else:
                return 0
    return sum_val

ans = 0

for x in range(2, n):
    for y in range(1, n - 1):
        for r in range(1, n):
            for c in range(1, n):
                ans = max(ans, sum_value(r, c, x, y))

print(ans)