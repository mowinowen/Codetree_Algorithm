import sys
from itertools import product
input = sys.stdin.readline

expression = input().strip()

# Please write your code here.
operators = expression[1::2]
operands = expression[::2]
set_operands = list(set(operands))

ans = float('-inf')
for nums in product(range(1, 5), repeat = len(set_operands)):
    num_map = dict(zip(set_operands, nums))

    sum_val = num_map[set_operands[0]]
    
    for op, ch in zip(operators, operands[1:]):
        if op == '+':
            sum_val += num_map[ch]
        elif op == '-':
            sum_val -= num_map[ch]
        else:
            sum_val *= num_map[ch]

    ans = max(ans, sum_val)

print(ans)