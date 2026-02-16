import sys
input = sys.stdin.readline

n = int(input())

# Please write your code here.
result = []
visited = [0] * n

def dfs(cnt):
    if cnt == n:
        print(*result)
        return
    
    for i in range(n, 0, -1):
        if not visited[i - 1]:
            result.append(i)
            visited[i - 1] = 1
            dfs(cnt + 1)
            result.pop()
            visited[i - 1] = 0

dfs(0)