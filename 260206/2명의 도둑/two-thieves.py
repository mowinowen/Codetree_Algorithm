import sys
from itertools import combinations
input = sys.stdin.readline

n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
info = []
for i in range(n):
    for j in range(n - m + 1):
        seg_weight = weight[i][j : j + m]
        max_val = 0

        for num in range(1, m + 1):
            for comb in combinations(seg_weight, num):
                if sum(comb) <= c:
                    max_val = max(sum(k ** 2 for k in comb), max_val)
        
        info.append((max_val, i, j))

ans = 0
for i in range(len(info)):
    for j in range(i + 1, len(info)):
        val1, i1, j1 = info[i]
        val2, i2, j2 = info[j]

        if not (i1 == i2 and j2 - j1 < m):
            ans = max(ans, val1 + val2)

print(ans)