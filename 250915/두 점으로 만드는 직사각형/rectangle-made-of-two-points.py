x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
min_x, max_x = min(x1, a1), max(x2, a2)
min_y, max_y = min(y1, b1), max(y2, b2)

print((max_x - min_x) * (max_y - min_y))