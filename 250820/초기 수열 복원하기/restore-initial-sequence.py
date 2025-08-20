n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.
arr = [0] * n

for i in range(1, n + 1):
    arr[0] = i
    isbool = True
    for j in range(n - 1):
        arr[j + 1] = adjacent[j] - arr[j]
        if arr[j + 1] < 1:
            isbool = False
            break
    
    if isbool:
        if len(set(arr)) == n:
            break

print(*arr)
