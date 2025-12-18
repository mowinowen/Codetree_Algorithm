import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
a = [[-1] * m] + [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def shift(d, r):
    if d == 'L':
        a[r] = a[r][-1:] + a[r][:-1]
    else:
        a[r] = a[r][1:] + a[r][:1]

for _ in range(q):
    r, d = input().split()
    r = int(r)
    shift(d, r)

    curr_r, curr_d = r, d
    while curr_r > 1 and any(a[curr_r][i] == a[curr_r - 1][i] for i in range(m)):
        curr_r -= 1
        curr_d = 'R' if curr_d == 'L' else 'L'
        shift(curr_d, curr_r)

    curr_r, curr_d = r, d
    while curr_r < n and any(a[curr_r][i] == a[curr_r + 1][i] for i in range(m)):
        curr_r += 1
        curr_d = 'R' if curr_d == 'L' else 'L'
        shift(curr_d, curr_r)

for row in a[1:]:
    print(*row)
