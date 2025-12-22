n = int(input())
grid = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

tmp = grid[r][c]
cur_r, cur_c = r, c
if dir == 0:
    for i in range(1, m4 + 1):
        grid[cur_r - i + 1][cur_c - i + 1] = grid[cur_r - i][cur_c - i]
    cur_r, cur_c = cur_r - m4, cur_c - m4
    
    for i in range(1, m3 + 1):
        grid[cur_r - i + 1][cur_c + i - 1] = grid[cur_r - i][cur_c + i]
    cur_r, cur_c = cur_r - m3, cur_c + m3

    for i in range(1, m2 + 1):
        grid[cur_r + i - 1][cur_c + i - 1] = grid[cur_r + i][cur_c + i]
    cur_r, cur_c = cur_r + m2, cur_c + m2

    for i in range(1, m1):
        grid[cur_r + i - 1][cur_c - i + 1] = grid[cur_r + i][cur_c - i]
    grid[r - 1][c + 1] = tmp

else:
    for i in range(1, m1 + 1):
        grid[cur_r - i + 1][cur_c + i - 1] = grid[cur_r - i][cur_c + i]
    cur_r, cur_c = cur_r - m1, cur_c + m1

    for i in range(1, m2 + 1):
        grid[cur_r - i + 1][cur_c - i + 1] = grid[cur_r - i][cur_c - i]
    cur_r, cur_c = cur_r - m2, cur_c - m2

    for i in range(1, m3 + 1):
        grid[cur_r + i - 1][cur_c - i + 1] = grid[cur_r + i][cur_c - i]
    cur_r, cur_c = cur_r + m3, cur_c - m3

    for i in range(1, m4):
        grid[cur_r + i - 1][cur_c + i - 1] = grid[cur_r + i][cur_c + i]
    grid[r - 1][c - 1] = tmp
    
for row in grid[1:]:
    print(*row[1:])