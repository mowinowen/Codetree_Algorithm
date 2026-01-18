import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [[[num] for num in list(map(int, input().split()))] for _ in range(n)]
move_nums = list(map(int, input().split()))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for num in move_nums:
    ismove = False
    for i in range(n):
        for j in range(n):
            if num in grid[i][j]:
                max_num = 0
                num_idx = grid[i][j].index(num)
                max_x, max_y = i, j
                for dx, dy in dirs:
                    if 0 <= i + dx < n and 0 <= j + dy < n and len(grid[i + dx][j + dy]) != 0:
                        curr_max = max(grid[i + dx][j + dy])
                        if max_num < curr_max:
                            max_num = curr_max
                            max_x, max_y = i + dx, j + dy
                
                # print(max_x, max_y, num)
                
                # for k in range(num_idx, -1, -1):
                #     grid[max_x][max_y].appendleft(grid[i][j][k])
                
                grid[max_x][max_y] = grid[i][j][:num_idx + 1] + grid[max_x][max_y]
                del grid[i][j][:num_idx + 1]

                # print(grid)
                ismove = True
            
            if ismove:
                break
        
        if ismove:
            break

for row in grid:
    for cell in row:
        if cell:
            print(*cell)
        else:
            print('None')