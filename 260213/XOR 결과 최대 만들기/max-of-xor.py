import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
ans = 0
def dfs(idx, curr, cnt):
    global ans
    if cnt == m:
        ans = max(ans, curr)
        return
    
    for i in range(idx, n):
        dfs(i + 1, curr ^ A[i], cnt + 1)

dfs(0, 0, 0)
print(ans)