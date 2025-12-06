n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def sum_value(r, c, x, y):
    sum_val = 0
    for _ in range(1, r + 1):
        if in_range(x + d[0][0], y + d[0][1]):
            x, y = x + d[0][0], y + d[0][1]
            sum_val += grid[x][y]
        else:
            return 0
    
    for _ in range(1, c + 1):
        if in_range(x + d[1][0], y + d[1][1]):
            x, y = x + d[1][0], y + d[1][1]
            sum_val += grid[x][y]
        else:
            return 0

    for _ in range(1, r + 1):
        if in_range(x + d[2][0], y + d[2][1]):
            x, y = x + d[2][0], y + d[2][1]
            sum_val += grid[x][y]
        else:
            return 0
    
    for _ in range(1, c + 1):
        if in_range(x + d[3][0], y + d[3][1]):
            x, y = x + d[3][0], y + d[3][1]
            sum_val += grid[x][y]
        else:
            return 0
    
    return sum_val

ans = 0
d = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
for x in range(n):
    for y in range(n):
        for r in range(1, n):
            for c in range(1, n):
                ans = max(ans, sum_value(r, c, x, y))

print(ans)