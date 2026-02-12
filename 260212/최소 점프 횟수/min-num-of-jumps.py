import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
result = [0]
ans = float('inf')

def dfs(cnt):
    global ans
    if cnt >= n - 1:
        ans = min(ans, len(result) - 1)
        return
    
    for i in range(1, num[cnt] + 1):
        result.append(cnt + i)
        dfs(cnt + i)
        result.pop()

dfs(0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)