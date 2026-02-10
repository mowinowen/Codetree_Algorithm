import sys
input = sys.stdin.readline

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
moves = [-1, (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
start_x, start_y = r - 1, c - 1
ans = 0

def dfs(cnt, x, y):
    global ans
    dx, dy = moves[move_dir[x][y]]
    for i in range(1, n):
        nx, ny = x + dx * i, y + dy * i

        if 0 <= nx < n and 0 <= ny < n:
            if num[nx][ny] > num[x][y]:
                ans = max(cnt, ans)
                dfs(cnt + 1, nx, ny)

dfs(1, r - 1, c - 1)
print(ans)