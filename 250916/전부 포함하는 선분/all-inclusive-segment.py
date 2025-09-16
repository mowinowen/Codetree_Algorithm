n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.

sort_start_arr = sorted(arr)
min_x1, min_x2 = sort_start_arr[0][0], sort_start_arr[1][0]

sort_end_arr = sorted(arr, key = lambda x : x[1])
max_x1, max_x2 = sort_end_arr[-1][1], sort_end_arr[-2][1]

print(min(max_x2 - min_x1, max_x1 - min_x2))