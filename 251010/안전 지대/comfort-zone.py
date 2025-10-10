n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt = 0
# l = []
max_k = 0
for row in grid:
    max_k = max(max_k, max(row))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y, height):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] <= height:
        return False
    return True

def dfs(x, y, height):
    global cnt
    visited[x][y] = True
    cnt += 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y +dy
        if can_go(new_x, new_y, height):
            dfs(new_x, new_y, height)

ans_list = []
for k in range(1, max_k + 1):
    visited = [[False] * m for _ in range(n)]
    l = []
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                cnt = 0
                dfs(i, j, k)
                l.append(cnt)

    # print(k, l)
    ans_list.append((k, len(l)))

print(*sorted(ans_list, key = lambda x : (-x[1], x[0]))[0])