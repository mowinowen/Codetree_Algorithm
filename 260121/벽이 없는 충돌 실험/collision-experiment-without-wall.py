import sys
input = sys.stdin.readline

T = int(input())

dirs = {'L' : (-1, 0), 'R' : (1, 0), 'U' : (0, 1), 'D' : (0, -1)}

for _ in range(T):
    n = int(input())
    info = []
    for i in range(n):
        x, y, w, d = input().split()
        info.append((int(x) * 2, int(y) * 2, int(w), i + 1, d))
    
    last_time = -1
    
    for t in range(1, 4002):
        if len(info) < 2:
            break
        
        marbles = {}
        for x, y, w, i, d in info:
            dx, dy = dirs[d]
            if (x + dx, y + dy) not in marbles:
                marbles[(x + dx, y + dy)] = []
            marbles[(x + dx, y + dy)].append((w, i, d))
        
        isbomb = False
        info = []
        for pos, infos in marbles.items():
            if len(infos) > 1:
                isbomb = True
                max_val = max(infos, key = lambda x : (x[0], x[1]))
                info.append((pos[0], pos[1], max_val[0], max_val[1], max_val[2]))
            else:
                info.append((pos[0], pos[1], infos[0][0], infos[0][1], infos[0][2]))
        
        if isbomb:
            last_time = t
    
    print(last_time)