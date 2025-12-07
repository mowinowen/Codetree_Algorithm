n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.    

rec_list = []
for x in range(n):
    for y in range(m):
        for a in range(n):
            for b in range(m):
                if x + a < n and y + b < m:
                    sum_val = 0
                    for i in range(x, x + a + 1):
                        for j in range(y, y + b + 1):
                            sum_val += grid[i][j]
                    rec_list.append(((x, y, x + a, y + b), sum_val))

ans = float('-inf')

for i in range(len(rec_list)):
    pos, sum_val1 = rec_list[i]
    x1, y1, x2, y2 = pos[0], pos[1], pos[2], pos[3]
    visited = [[0] * m for _ in range(n)]
    
    for j in range(i + 1, len(rec_list)):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                visited[x][y] = 1
        pos, sum_val2 = rec_list[j]
        x3, y3, x4, y4= pos[0], pos[1], pos[2], pos[3]

        isoverlap = False
        for x in range(x3, x4 + 1):
            for y in range(y3, y4 + 1):
                if visited[x][y]:
                    isoverlap = True
                    break
            if isoverlap:
                break
        
        if not isoverlap:
            ans = max(ans, sum_val1+sum_val2)

print(ans)