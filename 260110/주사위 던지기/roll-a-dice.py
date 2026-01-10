import sys
input = sys.stdin.readline

n, m, r, c = map(int, input().split())
directions = list(input().strip().split())

# Please write your code here.
grid = [[0] * n for _ in range(n)]
x, y, num = r - 1, c - 1, 6
grid[x][y] = num
dice = {'top' : 1, 'front' : 2, 'back' : 5, 'left' : 4, 'right' : 3}

for d in directions:
    tmp = num
    if d == 'L':
        if 0 <= x < n and 0 <= y - 1 < n:
            num = dice['left']
            dice['left'] = dice['top']
            dice['top'] = dice['right']
            dice['right'] = tmp
            y -= 1
    elif d == 'R':
        if 0 <= x < n and 0 <= y + 1 < n:
            num = dice['right']
            dice['right'] = dice['top']
            dice['top'] = dice['left']
            dice['left'] = tmp
            y += 1
    elif d == 'D':
        if 0 <= x + 1 < n and 0 <= y < n:
            num = dice['front']
            dice['front'] = dice['top']
            dice['top'] = dice['back']
            dice['back'] = tmp
            x += 1
    elif d == 'U':
        if 0 <= x - 1 < n and 0 <= y < n:
            num = dice['back']
            dice['back'] = dice['top']
            dice['top'] = dice['front']
            dice['front'] = tmp
            x -= 1

    grid[x][y] = num

print(sum(sum(row) for row in grid))