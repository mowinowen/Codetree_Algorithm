import sys
input = sys.stdin.readline

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
full = u + d
t %= 2 * n

full = full[-t:] + full[:-t]

print(*full[:n])
print(*full[n:])