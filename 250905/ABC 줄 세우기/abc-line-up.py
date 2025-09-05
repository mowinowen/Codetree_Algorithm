n = int(input())
arr = list(input().split())

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if ord(arr[i]) - ord('A') > ord(arr[j]) - ord('A'):
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1

print(cnt)