import heapq

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2 + 1][y2 + 1] - prefix_sum[x1][y2 + 1] - prefix_sum[x2 + 1][y1] + prefix_sum[x1][y1]

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + grid[i - 1][j - 1]

arr = []
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                arr.append((x1, y1, x2, y2, get_sum(x1, y1, x2, y2)))

ans = float('-inf')
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        x1, y1, x2, y2, s1 = arr[i]
        x3, y3, x4, y4, s2 = arr[j]

        if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
            ans = max(ans, s1 + s2)

print(ans)