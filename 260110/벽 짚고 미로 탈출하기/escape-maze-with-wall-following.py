import sys
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())

grid = list(input().strip() for _ in range(N))

# Please write your code here.
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
visited = set()

x, y, d = x - 1, y - 1, 0
ans = 0
while 0 <= x < N and 0 <= y < N:
    if (x, y, d) in visited:
        print(-1)
        break

    visited.add((x, y, d))
    r_dx, r_dy = dirs[(d + 3) % 4]

    wall_x, wall_y = x + r_dx, y + r_dy
    if 0 <= wall_x < N and 0 <= wall_y < N and grid[x + r_dx][y + r_dy] == '#':
        dx, dy = dirs[d]
        if 0 <= x + dx < N and 0 <= y + dy < N and grid[x + dx][y + dy] == '#':
            d = (d + 1) % 4
        else:
            x, y = x + dx, y + dy
            ans += 1

    else:
        d = (d + 3) % 4
        dx, dy = dirs[d]
        x, y = x + dx, y + dy
        ans += 1

else:
    print(ans)