import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = sys.maxsize
for i in arr:
    idxs = [j for j, val in enumerate(arr) if val <= i]

    if idxs[0] == 0 and idxs[-1] == n - 1 and all(idxs[j] - idxs[j - 1] <= k for j in range(1, len(idxs))):
        ans = min(ans, i)

print(ans)