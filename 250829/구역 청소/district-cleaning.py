a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
if b < c or d < a:
    print(b - a + d - c)

else:
    print(max(a, b, c, d) - min(a, b, c, d))