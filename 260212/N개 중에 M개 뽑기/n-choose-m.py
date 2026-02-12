import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# Please write your code here.
result = []

def dfs(num):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(num, N + 1):
        result.append(i)
        dfs(i + 1)
        result.pop()

dfs(1)