n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def number_counting(arr):
    cnt = 0
    curr = 1
    max_cnt = 1
    for i in range(1, n):
        if arr[i - 1] == arr[i]:
            curr += 1
            max_cnt = max(max_cnt, curr)
        else:
            curr = 1

    if max_cnt >= m:
        cnt += 1

    return cnt


ans = 0
for row in grid:
    ans += number_counting(row)

for col in zip(*grid):
    ans += number_counting(col)
print(ans)