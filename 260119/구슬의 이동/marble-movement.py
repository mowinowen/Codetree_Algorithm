import sys
input = sys.stdin.readline

n, m, t, k = map(int, input().split())
marbles = {}
new_marbles = {}
grid = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, d, v = input().split()
    r, c, v = int(r), int(c), int(v)

    marbles[i + 1] = (r - 1, c - 1, d, v)
    grid[r - 1][c - 1] = [(i + 1, v)]

dirs = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}
ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]
reverse_dirs = [1, 0, 3, 2]

for _ in range(t):
    for (num, (r, c, d, v)) in marbles.items():
        idx = grid[r][c].index((num, v))
        nr, nc = r, c
        for _ in range(v):
            d_num = dirs[d]
            dx, dy = ds[d_num]

            if 0 <= nr + dx < n and 0 <= nc + dy < n:
                nr, nc = nr + dx, nc + dy
            else:
                d_num = reverse_dirs[dirs[d]]
                d = list(dirs.keys())[d_num]
                dx, dy = ds[d_num]

                nr, nc = nr + dx, nc + dy
    
        new_marbles[num] = (nr, nc, d, v)
        grid[nr][nc].append((num, v))

        grid[r][c] = grid[r][c][:idx] + grid[r][c][idx + 1:]
    
    for x in range(n):
        for y in range(n):
            if len(grid[x][y]) > k:
                chunk = grid[x][y]
                chunk = sorted(chunk, key = lambda x : (-x[1], -x[0]))
                for i in range(len(chunk), k, -1):
                    num, v = grid[x][y].pop()
                    del new_marbles[num]

    marbles = new_marbles
   
cnt = 0
# print(grid)
for row in grid:
    for marble in row:
        # print(marble)
        if marble:
            # print(marble)
            cnt += len(marble)

print(cnt)