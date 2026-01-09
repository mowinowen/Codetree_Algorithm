N = int(input())
x, y = map(int, input().split())

grid = list(list(input()) for _ in range(N))

# Please write your code here.
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
visited = [[[0] * 4 for _ in range(N)]  for _ in range(N)]

x, y = x - 1, y - 1
dir_idx = 0
ans = 0
while True:
    r_dx, r_dy = dirs[(dir_idx + 3) % 4]
    visited[x][y][dir_idx] = 1

    if grid[x + r_dx][y + r_dy] == '#':
        dx, dy = dirs[dir_idx]
        if 0 <= x + dx < N and 0 <= y + dy < N and grid[x + dx][y + dy] == '#':
            dir_idx = (dir_idx + 1) % 4
        else:
            x = x + dx
            y = y + dy
            ans += 1

    else:
        dir_idx = (dir_idx + 3) % 4
        dx, dy = dirs[dir_idx]

        x = x + dx
        y = y + dy
        ans += 1

    if not (0 <= x < N and 0 <= y < N):
        print(ans)
        break
    else:
        if visited[x][y][dir_idx]:
            print(-1)
            break
