import math

X = int(input())

# Please write your code here.
max_v = math.sqrt(X)
if int(max_v) < max_v < int(max_v) + 1:
    print(2 * int(max_v))
else:
    print(2 * int(max_v) - 1)