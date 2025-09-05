n = int(input())
arr = list(input().split())

# Please write your code here.
cnt = sum(i == ord(val) - ord('A') for i, val in enumerate(arr))

print(n - cnt - 1)