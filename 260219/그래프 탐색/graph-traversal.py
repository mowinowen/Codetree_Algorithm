import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for x, y in edges:
    graph[x].append(y)
    graph[y].append(x)

ans = 0
def dfs(v):
    global ans
    for i in graph[v]:
        if not visited[i]:
            ans += 1
            visited[i] = 1
            dfs(i)

visited[1] = 1
dfs(1)
print(ans)