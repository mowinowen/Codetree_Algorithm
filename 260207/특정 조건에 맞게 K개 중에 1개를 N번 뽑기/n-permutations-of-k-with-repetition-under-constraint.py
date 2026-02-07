import sys
from itertools import product

input = sys.stdin.readline
K, N = map(int, input().split())

# Please write your code here.
for nums in product(range(1, K + 1), repeat = N):
    if len(nums) > 2:
        if all(not (nums[i] == nums[i + 1] == nums[i + 2]) for i in range(N - 2)):
            print(*nums)
    else:
        print(*nums)
