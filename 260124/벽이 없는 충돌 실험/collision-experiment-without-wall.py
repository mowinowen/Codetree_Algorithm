import sys
input = sys.stdin.readline

T = int(input())

dirs = {'L' : (-1, 0), 'R' : (1, 0), 'U' : (0, 1), 'D' : (0, -1)}

for _ in range(T):
    n = int(input())
    info = []
    for i in range(n):
        x, y, w, d = input().split()
        info.append([int(x) * 2, int(y) * 2, int(w), i + 1, d, True])
        
    collisions = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, w1, num1, d1, _ = info[i]
            x2, y2, w2, num2, d2, _ = info[j]

            dx1, dy1 = dirs[d1]
            dx2, dy2 = dirs[d2]

            if d1 == d2:
                continue
            elif (d1 == 'L' and d2 == 'R') or (d1 == 'R' and d2 == 'L'):
                if y1 != y2:
                    continue
                else:
                    if (-x1 + x2) // (dx1 - dx2) > 0:
                        collisions.append([(x1, y1, w1, num1), (x2, y2, w2, num2), (-x1 + x2) // (dx1 - dx2)])
            elif (d1 == 'U' and d2 == 'D') or (d1 == 'D' and d2 == 'U'):
                if x1 != x2:
                    continue
                else:
                    if (-y1 + y2) // (dy1 - dy2) > 0:
                        collisions.append([(x1, y1, w1, num1), (x2, y2, w2, num2), (-y1 + y2) // (dy1 - dy2)])
            else:
                if (-x1 + x2) // (dx1 - dx2) == (-y1 + y2) // (dy1 - dy2):
                    if (-x1 + x2) // (dx1 - dx2) > 0 and (-y1 + y2) // (dy1 - dy2) > 0:
                        collisions.append([(x1, y1, w1, num1), (x2, y2, w2, num2), (-y1 + y2) // (dy1 - dy2)])
            
    collisions.sort(key = lambda x : x[2])

    ans = -1
    for m1, m2, time in collisions:
        if info[m1[3] - 1][-1] and info[m2[3] - 1][-1]:
            ans = time
        else:
            continue
        
        if m1[2] < m2[2]:
            info[m1[3] - 1][-1] = False
        
        elif m1[2] > m2[2]:
            info[m2[3] - 1][-1] = False

        else:
            if m1[3] < m2[3]:
                info[m1[3] - 1][-1] = False
            else:
                info[m2[3] - 1][-1] = False

    print(ans)