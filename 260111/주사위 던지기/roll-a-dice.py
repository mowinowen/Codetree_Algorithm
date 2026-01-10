import sys
input = sys.stdin.readline

n, m, r, c = map(int, input().split())
directions = list(input().strip().split())

# Please write your code here.
grid = [[0] * n for _ in range(n)]
x, y= r - 1, c - 1
top, front, right, left, back, bottom = 1, 2, 3, 4, 5, 6
grid[x][y] = bottom
dirs = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}

for d in directions:
    dx, dy = dirs[d]
    nx, ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < n:
        if d == 'L':
            bottom, left, top, right = left, top, right, bottom
        elif d == 'R':
            bottom, right, top, left = right, top, left, bottom
        elif d == 'D':
            bottom, front, top, back = front, top, back, bottom
        elif d == 'U':
            bottom, back, top, front = back, top, front, bottom

        grid[nx][ny] = bottom
        x, y = nx, ny

print(sum(sum(row) for row in grid))