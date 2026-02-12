import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
ans = n - 1
cnt = 0

def dfs(idx):
    global ans, cnt
    if idx >= n - 1:
        ans = min(ans, cnt)
        return
    
    for i in range(1, num[idx] + 1):
        cnt += 1
        dfs(idx + i)
        cnt -= 1

dfs(0)
print(-1 if ans == n - 1 else ans)