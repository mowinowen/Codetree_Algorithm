n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def mining_shape_0(x, y):
    return grid[x][y]

def mining_shape_1(x, y):
    d = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    
    sum_val = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]:
            sum_val += 1
    
    if 5 <= sum_val * m:
        return sum_val
    
    else:
        return 0

def mining_shape_2(x, y):
    d = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 2), (0, -2), (2, 0), (-2, 0)]

    sum_val = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]:
            sum_val += 1

    if 13 <= sum_val * m:
        return sum_val
    
    else:
        return 0


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(mining_shape_0(i, j), mining_shape_1(i, j), mining_shape_2(i, j), ans)

print(ans)