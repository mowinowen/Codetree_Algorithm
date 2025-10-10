n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = -1
# Please write your code here.
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                cnt = 0
                isanswer = True
                for x in range(i, k + 1):
                    for y in range(j, l + 1):
                        if grid[x][y] <= 0:
                            isanswer = False
                            break
                        cnt += 1
                    # print(i, j, k, l)
                    if isanswer:
                        ans = max(ans, cnt)

print(ans)