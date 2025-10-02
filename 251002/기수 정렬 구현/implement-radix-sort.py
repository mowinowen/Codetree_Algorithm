n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(6):
    radix_arr = [[] for _ in range(10)]
    for num in arr:
        radix_arr[num % 10 ** (i + 1) // 10 ** i].append(num)
    arr = [num for r in radix_arr for num in r]

print(*arr)