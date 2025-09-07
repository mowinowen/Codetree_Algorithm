n = int(input())
a, b, c = 0, 0, 0
curr = ''
ans = 0

for _ in range(n):
    ci, si = input().split()
    si = int(si)
    if ci == 'A':
        a += si
    elif ci == 'B':
        b += si
    else:
        c += si
    
    if a > b and a > c:
        if curr != 'A':
            ans += 1
        curr = 'A'
    
    elif b > a and b > c:
        if curr != 'B':
            ans += 1
        curr = 'B'
    
    elif c > b and c > a:
        if curr != 'C':
            ans += 1
        curr = 'C'
    
    elif a == b and a > c:
        if curr != 'AB':
            ans += 1
        curr = 'AB'
    
    elif a == c and a > b:
        if curr != 'AC':
            ans += 1
        curr = 'AC'
    
    elif b == c and b > a:
        if curr != 'BC':
            ans += 1
        curr = 'BC'
    
    else:
        if curr != 'ABC':
            ans += 1
        curr = 'ABC'

print(ans)