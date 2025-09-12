arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
print(arr[0], arr[1], arr[-1] - arr[0] - arr[1])