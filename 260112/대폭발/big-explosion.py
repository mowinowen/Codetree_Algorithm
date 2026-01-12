import sys
input = sys.stdin.readline

n, m, r, c = map(int, input().split())

# Please write your code here.

visited = {(r - 1, c - 1)}
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for t in range(1, m + 1):
    tmp = set()
    for x, y in visited:
        for dx, dy in dirs:
            nx, ny = x + dx * (2 ** (t - 1)), y + dy * (2 ** (t - 1))
            if 0 <= nx < n and 0 <= ny < n:
                tmp.add((nx, ny))
    
    visited.update(tmp)

print(len(visited))