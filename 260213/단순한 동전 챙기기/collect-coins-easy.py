import sys
input = sys.stdin.readline

n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
num_dict = {}
for i in range(n):
    for j in range(n):
        if grid[i][j].isdigit():
            num_dict[int(grid[i][j])] = (i, j)
        
        elif grid[i][j] == 'S':
            start = (i, j)
        
        elif grid[i][j] == 'E':
            end = (i, j)

num_keys = sorted(list(num_dict.keys()))
ans = float('inf')
def dfs(num, cnt, pos, curr):
    global ans
    if cnt == 3:
        ans = min(ans, curr + abs(pos[0] - end[0]) + abs(pos[1] - end[1]))
        return
    
    for i in range(num, len(num_keys)):
        dfs(i + 1, cnt + 1, num_dict[num_keys[i]], curr + abs(pos[0] - num_dict[num_keys[i]][0]) + abs(pos[1] - num_dict[num_keys[i]][1]))
    
dfs(0, 0, start, 0)
print(-1 if ans == float('inf') else ans)