import sys
input = sys.stdin.readline

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    temp1, temp2 = u[n - 1], d[n - 1]
    for i in range(n - 2, -1, -1):
        u[i + 1] = u[i]
        d[i + 1] = d[i]
    
    d[0], u[0] = temp1, temp2

print(*u)
print(*d)