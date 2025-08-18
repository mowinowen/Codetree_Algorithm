N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
arr.sort()

ans = 0
j = 0
for i in range(N):
    while j < N and arr[j] - arr[i] <= K:
        j += 1
    ans = max(ans, j - i)

print(ans)