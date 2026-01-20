import sys
input = sys.stdin.readline

n, m, t, k = map(int, input().split())
marbles = []
dirs = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}
ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for i in range(m):
    r, c, d, v = input().split()
    marbles.append([int(r) - 1, int(c) - 1, dirs[d], int(v), i + 1])

for _ in range(t):
    next_pos = {}

    for r, c, d, v, num in marbles:
        move_cnt = v % ((n - 1) * 2)
        for _ in range(move_cnt):
            dx, dy = ds[d]
            nr, nc = r + dx, c + dy

            if not (0 <= nr < n and 0 <= nc < n):
                d ^= 1
                dx, dy = ds[d]
                nr, nc = r + dx, c + dy
            
            r, c = nr, nc

        if (r, c) not in next_pos:
            next_pos[(r, c)] = []
        
        next_pos[(r, c)].append([r, c, d, v, num])
    
    marbles = []
    for items in next_pos.values():
        if len(items) > k:
            items.sort(key = lambda x : (-x[3], -x[4]))
            marbles.extend(items[:k])
        else:
            marbles.extend(items)

print(len(marbles))