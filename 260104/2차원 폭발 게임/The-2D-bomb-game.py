import sys
from itertools import groupby

input = sys.stdin.readline

n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for _ in range(k):
    new_grid = []
    for col in zip(*numbers_2d):
        while True:
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

    new_grid = list(map(list, zip(*new_grid)))
    numbers_2d = list(map(list, zip(*new_grid[::-1])))

    new_grid = []
    for col in zip(*numbers_2d):
        col = [c for c in col if c]
        while True:
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

    numbers_2d = list(map(list, zip(*new_grid)))

print(n ** 2 - sum(row.count(0) for row in numbers_2d))