import sys
from itertools import product
input = sys.stdin.readline

K, N = map(int, input().split())

# Please write your code here.
for val in product([i for i in range(1, K + 1)], repeat = N):
    print(*val)