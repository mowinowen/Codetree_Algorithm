n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()
ans = float('inf')
for i in range(n):
    ans = min(arr[i + n] - arr[i], ans)

print(ans)