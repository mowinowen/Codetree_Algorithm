import sys
input = sys.stdin.readline

T = int(input())
dirs = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}
reverse_dir = {'L' : 'R', 'R' : 'L', 'U' : 'D', 'D' : 'U'}

for _ in range(T):
    n, m = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    dir_grid = [[0] * n for _ in range(n)]
    
    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x), int(y)
        grid[x - 1][y - 1] = 1
        dir_grid[x - 1][y - 1] = d

    for _ in range(2 * n):
        next_cnt = [[0] * n for _ in range(n)]
        next_dir_grid = [[0] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    dx, dy = dirs[dir_grid[x][y]]
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        next_cnt[nx][ny] += 1
                        next_dir_grid[nx][ny] = dir_grid[x][y]
                    
                    else:
                        next_cnt[x][y] += 1
                        next_dir_grid[x][y] = reverse_dir[dir_grid[x][y]]
        
        # for row in next_cnt:
        #     print(*row)
        # print()
        # for row in next_dir_grid:
        #     print(*row)
        # print()

        for x in range(n):
            for y in range(n):
                if next_cnt[x][y] > 1:
                    next_cnt[x][y] = 0
                    next_dir_grid[x][y] = 0

        grid = next_cnt
        dir_grid = next_dir_grid

        # for row in grid:
        #     print(*row)
        # print()
        # for row in dir_grid:
        #     print(*row)
        # print()

    ans = 0
    for row in grid:
        ans += row.count(0)
    
    print(n ** 2 - sum(row.count(0) for row in grid))