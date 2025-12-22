import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())

# Create 2D array for building state
a = [[-1] * m] + [[-1] + list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

def in_range(x, y):
    return 0 < x < n + 1 and 0 < y < m + 1

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for r1, c1, r2, c2 in winds:
    tmp = a[r1][c1]

    for i in range(r1 + 1, r2 + 1):
        a[i - 1][c1] = a[i][c1]
    
    for i in range(c1 + 1, c2 + 1):
        a[r2][i - 1] = a[r2][i]
    
    for i in range(r2 - 1, r1 - 1, -1):
        a[i + 1][c2] = a[i][c2]

    for i in range(c2 - 1, c1, -1):
        a[r1][i + 1] = a[r1][i]
    
    a[r1][c1 + 1] = tmp

    update_val = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if r1 <= i <= r2 and c1 <= j <= c2:
                sum_val = a[i][j]
                cnt = 1

                for dx, dy in d:
                    if in_range(i + dx, j + dy):
                        sum_val += a[i + dx][j + dy]
                        cnt += 1
                update_val[(i, j)] = sum_val // cnt

    for (i, j), sum_val in update_val.items():
        a[i][j] = sum_val

for row in a[1:]:
    print(*row[1:])
