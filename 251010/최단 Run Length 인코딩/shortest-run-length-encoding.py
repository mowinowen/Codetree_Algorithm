import sys

A = input()

# Please write your code here.
ans = sys.maxsize
for i in range(len(A)):
    A = A[-1] + A[:-1]
    
    d = {A[0] : 1}
    s = ''
    for j in range(1, len(A)):
        if A[j] in d:
            d[A[j]] += 1
        else:
            s += A[j - 1]
            s += str(d[A[j - 1]])
            d = {A[j] : 1}
    
    for j in d:
        s += j
        s += str(d[j])
    ans = min(ans, len(s))

print(ans)