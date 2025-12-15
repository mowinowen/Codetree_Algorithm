import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = [0] * m
ans = -1

for _ in range(n):
    row = list(map(int, input().split()))
    
    for i in range(m):
        heights[i] = heights[i] + 1 if row[i] > 0 else 0

    for i in range(m):
        min_height = heights[i]
        for j in range(i, m):
            if heights[j] == 0:
                break
            min_height = min(min_height, heights[j])
            ans = max(min_height * (j - i + 1), ans)

print(ans)