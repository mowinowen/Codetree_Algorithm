import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(x - 1 for x in map(int, input().split())) for _ in range(m)]
dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for _ in range(t):
    curr_pos = set()
    for i in range(m):
        r, c = marbles[i]
        max_val = 0
        max_x, max_y = -1, -1
        for dx, dy in dirs:
            if 0 <= r + dx < n and 0 <= c + dy < n:
                if grid[r + dx][c + dy] > max_val:
                    max_val = grid[r + dx][c + dy]
                    max_x, max_y = r + dx, c + dy
        
        if (max_x, max_y) in curr_pos:
            curr_pos.remove((max_x, max_y))
        else:
            curr_pos.add((max_x, max_y))
    
    marbles = list(curr_pos)
    m = len(marbles)

print(m)