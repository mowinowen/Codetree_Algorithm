from itertools import product
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
ans = 0
for comb in product(range(1, k + 1), repeat = n):
    num_map = {}
    for i in range(1, k + 1):
        num_map[i] = 1
    
    cnt = 0
    for i in range(n):
        if num_map[comb[i]] >= m:
            continue
        num_map[comb[i]] += nums[i]

        if num_map[comb[i]] >= m:
            cnt += 1

    ans = max(cnt, ans)

print(ans)
