import sys
input = sys.stdin.readline

T = int(input())
mapper = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3}
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
reverse_dir = [1, 0, 3, 2]

for _ in range(T):
    n, m = map(int, input().split())
    marbles = {}
    
    for _ in range(m):
        x, y, d = input().split()
        marbles[(int(x) - 1, int(y) - 1)] = mapper[d]
        

    for _ in range(2 * n):
        next_marbles = {}
        bomb = set()

        for (x, y), d in marbles.items():
            dx, dy = dirs[d]
            nx, ny = x + dx, y + dy
            nd = d
            
            if not(0 <= nx < n and 0 <= ny < n):
                nd = reverse_dir[d]
                nx, ny = x, y

            if (nx, ny) in next_marbles:
                bomb.add((nx, ny))
            else:
                next_marbles[(nx, ny)] = nd
        
        for x, y in bomb:
            del next_marbles[(x, y)]
        
        marbles = next_marbles

        if not marbles:
            break

    print(len(marbles))