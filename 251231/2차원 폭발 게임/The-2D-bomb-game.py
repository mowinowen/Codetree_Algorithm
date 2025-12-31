import sys
from itertools import groupby

input = sys.stdin.readline

n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def bomb_grid(m):
    new_grid = []
    for col in zip(*numbers_2d):
        while True:
            new_col = []
            zero_cnt = 0
            for val, group in groupby(col):
                if val == 0:
                    new_col += list(group)
                    continue
                # cnt = len(list(group))
                group_list = list(group)
                if len(group_list) >= m:
                    zero_cnt += len(group_list)
                else:
                    # new_col.append(val)
                    new_col += group_list
            
            if zero_cnt == 0:
                break
            col = [0] * zero_cnt + new_col
        
        new_grid.append(col)

    return list(zip(*new_grid))


for _ in range(k):
    new_grid = bomb_grid(m)
    numbers_2d = list(map(list, zip(*new_grid[::-1])))

    new_grid = []
    for col in zip(*numbers_2d):
        new_col = [val for val in col if val]
        new_col = [0] * (n - len(new_col)) + new_col
        new_grid.append(new_col)

    numbers_2d = list(map(list, zip(*new_grid)))

    numbers_2d = bomb_grid(m)

ans = n ** 2 - sum(row.count(0) for row in numbers_2d)
print(ans)