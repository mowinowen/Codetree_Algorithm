from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 1

for i in range(2, n + 1):
    for comb in combinations(lines, i):
        points = []
        for x, y in comb:
            points.append((x, 1))
            points.append((y, -1))
        
        points.sort(key = lambda x : x[0])
        
        sum_cnt = 0
        isoverlap = False
        for _, cnt in points:
            sum_cnt += cnt
            if sum_cnt > 1:
                isoverlap = True
                break
        
        if not isoverlap:
            ans = max(ans, len(comb))

print(ans)