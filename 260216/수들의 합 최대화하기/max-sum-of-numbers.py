import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [0] * n
ans = 0
def dfs(cnt, curr):
    global ans
    if cnt == n:
        ans = max(ans, curr)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, curr + grid[i][cnt])
            visited[i] = 0

dfs(0, 0)
print(ans)
