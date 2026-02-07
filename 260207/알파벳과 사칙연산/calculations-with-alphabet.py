import sys
from itertools import product
input = sys.stdin.readline

expression = input().strip()

# Please write your code here.
operator = ['+'] + [e for e in expression if e in ['+', '-', '*']]
num_and_operator = [('+', expression[0])]
num_dict = {expression[0] : 0}

for i in range(1, len(expression) - 1, 2):
    num_and_operator.append((expression[i], expression[i + 1]))
    if not expression[i + 1] in num_dict:
        num_dict[expression[i + 1]] = 0

ans = float('-inf')
for nums in product(range(1, 5), repeat = len(num_dict)):
    for num, c in zip(nums,num_dict):
        num_dict[c] = num

    sum_num = 0
    for op, c in num_and_operator:
        if op == '+':
            sum_num += num_dict[c]
        elif op == '-':
            sum_num -= num_dict[c]
        else:
            sum_num *= num_dict[c]

    ans = max(ans, sum_num)

print(ans)
