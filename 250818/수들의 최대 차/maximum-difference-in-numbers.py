N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
arr.sort()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if arr[j] - arr[i] > K:
            ans = max(ans, j - i)
            break
print(ans)