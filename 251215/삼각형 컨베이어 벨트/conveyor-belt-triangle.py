n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
full = l + r + d
t %= 3 * n

full = full[-t:] + full[:-t]

for i in range(3):
    print(*full[n * i : n * i + n])