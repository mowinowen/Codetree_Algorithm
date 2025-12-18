from collections import deque

n, m, q = map(int, input().split())
a = [[0] * m] + [list(map(int, input().split())) for _ in range(n)] + [[0] * m]
# winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.

for _ in range(q):
    r, d = input().split()
    r = int(r)
    s = set()
    dq = deque()

    while True:
        # print(r, d)
        if d == 'L':
            a[r] = a[r][-1:] + a[r][:-1]
        
        else:
            a[r] = a[r][1:] + a[r][:1]

        # for row in a[1:-1]:
        #     print(*row)
        
        s.add(r)
        
        flag1 = False
        if r - 1 not in s:
            for i in range(m):
                if a[r][i] == a[r - 1][i]:
                    flag1 = True
        
        if flag1:
            dq.append((r - 1, 'R' if d == 'L' else 'L'))

        flag2 = False
        if r + 1 not in s:
            for i in range(m):
                if a[r][i] == a[r + 1][i]:
                    flag2 = True
        
        if flag2:
            dq.append((r + 1, 'R' if d == 'L' else 'L'))

        if len(dq) == 0:
            break

        r, d = dq.popleft()

for row in a[1:-1]:
    print(*row)