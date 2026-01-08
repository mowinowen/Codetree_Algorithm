n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

num = grid[r - 1][c - 1]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
x, y = r - 1, c - 1

while True:
    print(num, end = ' ')
    
    isend = True
    for dx, dy in dirs:
        if 0 <= x + dx < n and 0 <= y + dy < n:
            if num < grid[x + dx][y + dy]:
                x, y = x + dx, y + dy
                num = grid[x][y]
                isend = False
                break
    
    if isend:
        break