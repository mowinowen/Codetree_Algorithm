n = int(input())

max_left = float('-inf')
min_right = float('inf')
for _ in range(n):
    x1, x2 = map(int, input().split())
    max_left = max(max_left, x1)
    min_right = min(min_right, x2)

if max_left <= min_right:
    print('Yes')
else:
    print('No')