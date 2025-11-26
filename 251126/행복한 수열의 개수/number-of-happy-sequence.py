from itertools import groupby

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

print(sum(any(len(list(j)) >= m for i, j in groupby(row)) for row in grid + list(zip(*grid))))