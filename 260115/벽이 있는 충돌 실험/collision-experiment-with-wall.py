import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    marbles_pos = {}
    dirs = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}

    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x), int(y)
        marbles_pos[(x, y)] = d

    for _ in range(4 * n):
        new_marbles_pos = defaultdict(list)
        for x, y in marbles_pos:
            dx, dy = dirs[marbles_pos[(x, y)]]
            d = marbles_pos[(x, y)]
            
            if not (0 < x + dx <= n and 0 < y + dy <= n):
                if d == 'L':
                    d = 'R'
                elif d == 'R':
                    d = 'L'
                elif d == 'U':
                    d = 'D'
                else:
                    d = 'U'

                new_marbles_pos[(x, y)].append(d)
            
            else:
                new_marbles_pos[(x + dx, y + dy)].append(d)
        
        marbles_pos = {}
        for x, y in new_marbles_pos:
            if len(new_marbles_pos[(x, y)]) == 1:
                marbles_pos[(x, y)] = new_marbles_pos[(x, y)][0]
        
    print(len(marbles_pos))