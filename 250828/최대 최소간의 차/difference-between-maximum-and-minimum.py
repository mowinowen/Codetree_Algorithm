n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = float('inf')
min_val, max_val = min(arr), max(arr)
for i in range(min_val, max_val + 1):
    cost = 0
    for j in arr:
        if j < i:
            cost += i - j
        elif j > i + k:
            cost += j - i - k
    ans = min(cost, ans)

print(ans)