n = int(input())
a, b = 0, 0
curr = prev = 0
ans = 0
for _ in range(n):
    s, p = input().split()
    p = int(p)
    
    if s == 'A':
        a += p
    else:
        b += p
    
    if a < b:
        curr = 2
    elif a > b:
        curr = 1
    else:
        curr = 0
    
    if prev != curr:
        ans += 1
    
    prev = curr

print(ans)