n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = max(a), sum(a)
ans = right

while left <= right:
    mid = (left + right) // 2
    range_sum = 0
    cnt = 0
    range_sum_max = 0
    for j in a:
        if range_sum + j > mid:
            cnt += 1
            range_sum_max = max(range_sum_max, range_sum)
            range_sum = j
        else:
            range_sum += j
    
    cnt += 1
    range_sum_max = max(range_sum_max, range_sum)
    if cnt <= m:
        ans = min(ans, range_sum_max)
        right = mid - 1
    else:
        left = mid + 1

print(ans)