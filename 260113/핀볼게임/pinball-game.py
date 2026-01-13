import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def direction_change(d, x, y):
    if grid[x][y] == 1:
        d = d - 1 if d % 2 == 1 else d + 1
    
    elif grid[x][y] == 2:
        d = 3 - d
    
    return d

def move_pinball(d, x, y):
    move = 1
    d = direction_change(d, x, y)

    while True:
        move += 1
        dx, dy = dirs[d]
        x, y = x + dx, y + dy

        if not (0 <= x < n and 0 <= y < n):
            break

        d = direction_change(d, x, y)
    return max(ans, move)

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
ans = 0

for i in range(n):
    x, y = 0, i
    d = 0
    ans = move_pinball(d, x, y)

for i in range(n):
    x, y = i, n - 1
    d = 1
    ans = move_pinball(d, x, y)

for i in range(n):
    x, y = n - 1, i
    d = 2
    ans = move_pinball(d, x, y)

for i in range(n):
    x, y = i, 0
    d = 3
    ans = move_pinball(d, x, y)

print(ans)