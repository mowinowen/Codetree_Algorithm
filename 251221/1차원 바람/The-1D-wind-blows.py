import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
a = [[-1] * m] + [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def shift(d, r):
    if d == 'R':
        offset[r] = (offset[r] + 1) % m
    else:
        offset[r] = (offset[r] - 1 + m) % m

def row_compare(r1, r2):
    return any(a[r1][(i + offset[r1]) % m] == a[r2][(i + offset[r2]) % m] 
    for i in range(m))


offset = [0] * (n + 1)

for _ in range(q):
    r, d = input().split()
    r = int(r)
    shift(d, r)

    cur_r, cur_d = r, d
    while cur_r > 1 and row_compare(cur_r, cur_r - 1):
        cur_r -= 1
        cur_d = 'R' if cur_d == 'L' else 'L'
        shift(cur_d, cur_r)

    cur_r, cur_d = r, d
    while cur_r < n and row_compare(cur_r, cur_r + 1):
        cur_r += 1
        cur_d = 'R' if cur_d == 'L' else 'L'
        shift(cur_d, cur_r)
        
for i in range(1, n + 1):
    print(*(a[i][offset[i]:] + a[i][:offset[i]]))


'''
L : (idx + 1) % m
R : (idx - 1 + m) % m

0 1 2 3 4
1 2 3 4 0

3 L
a[3][(idx + 1) % m]
a[2][idx]

2 R
a[2][(idx - 1 + m) % m]
a[1][idx]

4 R
a[4][(idx - 1 + m) % m]
a[5][idx]

5 L
a[5][(idx + 1) % m]
a[6][idx]

3 L
2 R
1 L

1 L
2 R
3 L
'''