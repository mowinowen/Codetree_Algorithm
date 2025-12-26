import sys
input = sys.stdin.readline

# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input().strip()

# Please write your code here.
def update_grid(grid):
    new_grid = []
    for i in range(4):
        row = [num for num in grid[i] if num != 0]
        new_row = row + [0] * (4 - len(row))

        for i in range(1, 4):
            if new_row[i - 1] == new_row[i]:
                new_row[i - 1] *= 2
                new_row[i] = 0
                new_row = new_row[:i] + new_row[i + 1:] + [0]
        
        new_grid.append(new_row)

    return new_grid


if dir in 'UD':
    grid = list(zip(*grid))

if dir in 'RD':
    for i in range(4):
        grid[i] = grid[i][::-1]

new_grid = update_grid(grid)

if dir in 'RD':
    for i in range(4):
        new_grid[i] = new_grid[i][::-1]

if dir in 'UD':
    new_grid = list(zip(*new_grid))

for row in new_grid:
    print(*row)