import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
sum_val = sum(num)
ans = float('inf')
def dfs(idx, cnt, curr):
    global ans
    if cnt == n:
        ans = min(ans, abs(curr - abs(sum_val - curr)))
        return
    
    for i in range(idx, 2 * n):
        dfs(i + 1, cnt + 1, curr + num[i])

dfs(0, 0, 0)
print(ans)