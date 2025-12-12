n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.

def check_positive_rectangle(x1, y1, x2, y2):
    cnt = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if grid[x][y] > 0:
                 cnt += 1
            else:
                return -1

    return cnt

ans = -1
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1 + 1, n):
            for y2 in range(y1 + 1, m):
                ans = max(ans, check_positive_rectangle(x1, y1, x2, y2))

print(ans)