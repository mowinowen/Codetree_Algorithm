a, b, x, y = map(int, input().split())

# Please write your code here.
print(min(abs(b - a), abs(x - a) + abs(y - b), abs(x - b) + abs(y - a)))
