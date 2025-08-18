import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = sys.maxsize
for i in arr:
    idxs = []
    isbool = True
    for j, val in enumerate(arr):
        if val <= i:
            idxs.append(j)
    
    # print(idxs)
    if idxs[0] != 0 or idxs[-1] != n - 1:
        continue
    for j in range(1, len(idxs)):
        if idxs[j] - idxs[j - 1] > k:
            isbool = False
            break
    
    if isbool:
        ans = min(ans, i)

print(ans)