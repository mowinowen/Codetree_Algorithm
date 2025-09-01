import math

X = int(input())

# Please write your code here.
max_v = math.sqrt(X)
# print(max_v)

if int(max_v) == max_v:
    print(2 * int(max_v) - 1)
else:
    if 1 <= X - int(max_v) ** 2 <= int(max_v):
        print(2 * int(max_v))
    else:
        print(2 * int(max_v) + 1)