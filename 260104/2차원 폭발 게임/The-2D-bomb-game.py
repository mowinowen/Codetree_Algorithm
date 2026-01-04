import sys
from itertools import groupby

input = sys.stdin.readline

n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def bomb_grid(n, k):
    new_grid = []
    for col in zip(*numbers_2d):
        col = [c for c in col if c]
        while True:
            if not col:
                new_grid.append([0] * n)
                break
            new_col = []
            isbool = False
            for val, group in groupby(col):
                g_list = list(group)
                
                if len(g_list) >= m:
                    isbool = True
                else:
                    new_col += g_list
            
            col = new_col

            if not isbool:
                new_grid.append([0] * (n - len(col)) + col)
                break

    # numbers_2d = list(map(list, zip(*new_grid)))
    return list(map(list, zip(*new_grid)))

history = {}
for num in range(k):
    new_grid = bomb_grid(n, k)
    numbers_2d = list(map(list, zip(*new_grid[::-1])))
    numbers_2d = bomb_grid(n, k)

    # history[tuple(map(tuple, numbers_2d))] = num
    if tuple(map(tuple, numbers_2d)) in history:
        time = (k - num) % (num - history[tuple(map(tuple, numbers_2d))])

        for _ in range(time):
            new_grid = bomb_grid(n, k)
            numbers_2d = list(map(list, zip(*new_grid[::-1])))
            numbers_2d = bomb_grid(n, k)
        break
    
    history[tuple(map(tuple, numbers_2d))] = num
    
print(n ** 2 - sum(row.count(0) for row in numbers_2d))