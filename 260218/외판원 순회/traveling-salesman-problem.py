import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result = []
visited = [0] * n
ans = float('inf')

def dfs(cnt, curr, start):
    global ans
    if cnt == n - 1:
        ans = min(ans, curr + A[start][0])
        return
    
    for i in range(2, n + 1):
        if not visited[i - 1]:
            visited[i - 1] = 1
            dfs(cnt + 1, curr + A[start][i - 1], i - 1)
            visited[i - 1] = 0

dfs(0, 0, 0)
print(ans)