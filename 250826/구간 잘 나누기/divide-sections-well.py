n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
min_val, max_val = max(a), sum(a)
ans = max_val

for i in range(min_val, max_val + 1):
    range_sum = 0
    # range_sum_list = []
    cnt = 0
    range_sum_max = 0
    for j in a:
        if range_sum + j > i:
            # range_sum_list.append(range_sum)
            cnt += 1
            range_sum_max = max(range_sum_max, range_sum)
            range_sum = j
        else:
            range_sum += j
    
    # range_sum_list.append(range_sum)
    cnt += 1
    range_sum_max = max(range_sum_max, range_sum)
    # print(i, range_sum_list, cnt, range_sum_max)
    if cnt <= m:
        ans = min(ans, range_sum_max)
        # print(i, range_sum_list, cnt, range_sum_max)

print(ans)