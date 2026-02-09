import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

cnt_list = [1] * (k + 1)
ans = 0

def dfs(cnt):
    global ans
    if cnt == n:
        score = 0
        for i in range(1, k + 1):
            if cnt_list[i] >= m:
                score += 1
        ans = max(score, ans)
        return
    
    for i in range(1, k + 1):
        cnt_list[i] += nums[cnt]
        dfs(cnt + 1)
        cnt_list[i] -= nums[cnt]

dfs(0)
print(ans)