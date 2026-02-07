import sys
from itertools import product
input = sys.stdin.readline

expression = input().strip()

# Please write your code here.
operator = ['+'] + [e for e in expression if e in ['+', '-', '*']]

ans = float('-inf')
for nums in product(range(1, 5), repeat = len(operator)):
    sum_num = 0
    for i in range(len(operator)):
        if operator[i] == '+':
            sum_num += nums[i]
        elif operator[i] == '-':
            sum_num -= nums[i]
        else:
            sum_num *= nums[i]
    
    ans = max(ans, sum_num)

print(ans)