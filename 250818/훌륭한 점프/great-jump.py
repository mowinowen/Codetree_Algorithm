n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = n
for i in arr:
    idxs = []
    isbool = True
    for j, val in enumerate(arr):
        if val <= i:
            idxs.append(j)
    
    # print(idxs)
    if len(idxs) == 1:
        continue
    for j in range(1, len(idxs)):
        if idxs[j] - idxs[j - 1] > k:
            isbool = False
            break
    
    if isbool:
        ans = i

print(ans)