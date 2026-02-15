import sys
input = sys.stdin.readline

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dist_grid = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]

        dist_grid[i][j] = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2

result = []
ans = float('inf')

def dfs(idx, cnt):
    global ans
    if cnt == m:
        max_length = 0
        for i in range(m):
            for j in range(i + 1, m):
                max_length = max(max_length, dist_grid[result[i]][result[j]])
        
        ans = min(ans, max_length)
        return
    
    for i in range(idx, n):
        result.append(i)
        dfs(i + 1, cnt + 1)
        result.pop()

dfs(0, 0)
print(ans)
