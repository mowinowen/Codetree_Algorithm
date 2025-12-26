import sys
input = sys.stdin.readline

# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input().strip()

# Please write your code here.
new_grid = []
if dir == 'L':
    for i in range(4):
        row = grid[i]
        temp = [num for num in row if num != 0]
        temp = temp + [0] * (4 - len(temp))

        for i in range(1, 4):
            if temp[i - 1] == temp[i]:
                temp[i - 1] *= 2
                temp[i] = 0
                temp = temp[:i] + temp[i + 1:] + [0]
        
        new_grid.append(temp)

if dir == 'R':
    for i in range(4):
        row = grid[i]
        temp = [num for num in row if num != 0]
        temp = [0] * (4 - len(temp)) + temp

        for i in range(3, 0, -1):
            if temp[i - 1] == temp[i]:
                temp[i] *= 2
                temp[i - 1] = 0
                temp = [0] + temp[:i - 1] + temp[i:]
        
        new_grid.append(temp)

if dir == 'U':
    for col in zip(*grid):
        temp = [num for num in col if num != 0]
        temp = temp + [0] * (4 - len(temp))

        for i in range(1, 4):
            if temp[i - 1] == temp[i]:
                temp[i - 1] *= 2
                temp[i] = 0
                temp = temp[:i] + temp[i + 1:] + [0]
        
        new_grid.append(temp)
    new_grid = list(zip(*new_grid))

if dir == 'D':
    for col in zip(*grid):
        temp = [num for num in col if num != 0]
        temp = [0] * (4 - len(temp)) + temp

        for i in range(3, 0, -1):
            if temp[i - 1] == temp[i]:
                temp[i] *= 2
                temp[i - 1] = 0
                temp = [0] + temp[:i - 1] + temp[i:] 
        
        new_grid.append(temp)
    new_grid = list(zip(*new_grid))

for row in new_grid:
    print(*row)