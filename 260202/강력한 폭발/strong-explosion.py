import sys
from itertools import product

input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
bomb_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j]]
select_bomb = list(product([1, 2, 3], repeat = len(bomb_pos)))
info = {}
ans = 0

for select in select_bomb:
    bombs = set()
    for i in range(len(bomb_pos)):
        if (bomb_pos[i], select[i]) in info:
            tmp = info[(bomb_pos[i], select[i])]
        else:
            x, y = bomb_pos[i]
            tmp = []
            if select[i] == 1:                
                for k in range(-2, 3):
                    if 0 <= x + k < n and 0 <= y < n:
                        tmp.append((x + k, y))

            elif select[i] == 2:
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]:
                    if 0 <= x + dx < n and 0 <= y + dy < n:
                        tmp.append((x + dx, y + dy))

            else:
                for dx, dy in [(-1, -1), (1, 1), (-1, 1), (1, -1), (0, 0)]:
                    if 0 <= x + dx < n and 0 <= y + dy < n:
                        tmp.append((x + dx, y + dy))

            info[(bomb_pos[i], select[i])] = tmp

        for pos in tmp:
            bombs.add(pos)
    
    ans = max(ans, len(bombs))

print(ans)
