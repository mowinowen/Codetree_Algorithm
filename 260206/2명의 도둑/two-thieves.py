import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
info = []
for i in range(n):
    for j in range(n):
        curr = j
        sum_val = 0
        vals = []
        while curr < n:
            sum_val += weight[i][curr]
            if sum_val > c or len(vals) == m:
                break
            vals.append((i, curr))
            curr += 1

        info.append(vals)

ans = 0
for i in range(len(info)):
    for j in range(i + 1, len(info)):
        pos1 = info[i]
        pos2 = info[j]
        
        if not set(pos1) & set(pos2):
            sum_val = 0
            for x, y in pos1:
                sum_val += weight[x][y] ** 2
            for x, y in pos2:
                sum_val += weight[x][y] ** 2
        
            ans = max(ans, sum_val)

print(ans)