import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
K, N = map(int, input().split())

# Please write your code here.

result = []
def dfs(depth):
    if depth == N:
        print(*result)
        return
    
    for i in range(1, K + 1):
        if depth >= 2 and result[-1] == i and result[-2] == i:
            continue

        result.append(i)
        dfs(depth + 1)
        result.pop()

dfs(0)