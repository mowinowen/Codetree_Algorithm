n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.

sort_start_arr = sorted(arr)[1:]
ans = max(x for _, x in sort_start_arr) - sort_start_arr[0][0]

sort_end_arr = sorted(arr, key = lambda x : x[1])[:-1]
ans = min(ans, sort_end_arr[-1][1] - min(x for x, _ in sort_end_arr))
print(ans)