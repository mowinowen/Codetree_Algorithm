n = int(input())

max_left = float('-inf')
min_right = float('inf')
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    max_left = max(x1, max_left)
    min_right = min(x2, min_right)
    segments.append((x1, x2))

second_max_left = float('-inf')
second_min_right = float('inf')
for seg_x1, seg_x2 in segments:
    if seg_x1 != max_left:
        second_max_left = max(second_max_left, seg_x1)
    if seg_x2 != min_right:
        second_min_right = min(second_min_right, seg_x2)

if second_max_left <= min_right or max_left <= second_min_right:
    print('Yes')

else:
    print('No')