import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
result = []
ans = 0
def dfs(idx):
    global ans
    xor_val = 0
    if len(result) == m:
        xor_val = A[result[0]]
        for i in range(1, m):
            xor_val ^= A[result[i]]
        ans = max(ans, xor_val)
        return
    
    for i in range(idx, n):
        result.append(i)
        dfs(i + 1)
        result.pop()

dfs(0)
print(ans)