import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
mapper = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
info = []

for i in range(m):
    r, c, d, w = input().split()
    info.append([int(r), int(c), mapper[d], int(w), int(i + 1)])

for _ in range(t):
    info_dict = {}
    for r, c, d, w, i in info:
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc

        if not (0 < nr < n + 1 and 0 < nc < n + 1):
            d ^= 1
            nr, nc = r, c
        
        if (nr, nc) in info_dict:
            info_dict[(nr, nc)].append((d, w, i))
        else:
            info_dict[(nr, nc)] = [(d, w, i)]
    
    new_info = []
    for (r, c) in info_dict:
        if len(info_dict[(r, c)]) > 1:
            w = sum(w for _, w, _ in info_dict[(r, c)])
            d, i = info_dict[(r, c)][-1][0], info_dict[(r, c)][-1][-1]
        else:
            d, w, i = info_dict[(r, c)][0]
        new_info.append((r, c, d, w, i))
    
    info = new_info
    
print(len(info), max(marble[3] for marble in info))