x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
print(max(max(x2, a2) - min(x1, a1), max(y2, b2) - min(y1, b1)) ** 2)