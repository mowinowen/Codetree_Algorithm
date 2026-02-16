import sys
input = sys.stdin.readline

n = int(input())

# Please write your code here.
result = []

def dfs(cnt):
    if cnt == n:
        print(*result)
        return
    
    for i in range(1, n + 1):
        if i in result:
            continue
        result.append(i)
        dfs(cnt + 1)
        result.pop()

dfs(0)