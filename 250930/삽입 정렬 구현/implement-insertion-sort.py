n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    key = arr[i]
    for j in range(i - 1, -1, -1):
        if key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = key
        else:
            arr[j + 1] = key
            break

print(*arr)