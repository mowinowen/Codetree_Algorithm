n, m, q = map(int, input().split())

# Create 2D array for building state
a = [[-1] * m] + [[-1] + list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

def in_range(x, y):
    return 0 < x < n + 1 and 0 < y < m + 1

b = [[-1] * (m + 1) for _ in range(n + 1)]

for r1, c1, r2, c2 in winds:
    tmp = a[r1][c2]
    for i in range(c2 - 1, c1 - 1, -1):
        a[r1][i + 1] = a[r1][i]

    tmp2 = a[r2][c2]
    for i in range(r2 - 1, r1, -1):
        a[i + 1][c2] = a[i][c2]
    a[r1 + 1][c2] = tmp

    tmp3 = a[r2][c1]
    for i in range(c1 + 1, c2):
        a[r2][i - 1] = a[r2][i]
    a[r2][c2 - 1] = tmp2

    for i in range(r1 + 1, r2):
        a[i - 1][c1] = a[i][c1]
    a[r2 - 1][c1] = tmp3

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if r1 <= i <= r2 and c1 <= j <= c2:
                avg = a[i][j]
                cnt = 1
                if in_range(i + 1, j):
                    avg += a[i + 1][j]
                    cnt += 1
                if in_range(i - 1, j):
                    avg += a[i - 1][j]
                    cnt += 1
                if in_range(i, j + 1):
                    avg += a[i][j + 1]
                    cnt += 1
                if in_range(i, j - 1):
                    avg += a[i][j - 1]
                    cnt += 1
                
                b[i][j] = avg // cnt
            else:
                b[i][j] = a[i][j]
    
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            a[i][j] = b[i][j]

for row in b[1:]:
    print(*row[1:])

'''
3 1 3
2 2 1
3 3 3

2 2 3
2 1 1
3 3 3

2 2 3
2 3 1 
3 3 1

2 2 3
2 2 2
3 2 1

'''