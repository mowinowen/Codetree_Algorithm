import sys
input = sys.stdin.readline

A = input().strip()

# Please write your code here.
ans = float('inf')
for _ in range(len(A)):
    A = A[-1] + A[:-1]
    encoding = ''

    cnt = 0
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            encoding += A[i - 1] + str(i - cnt)
            cnt = i
    encoding += A[-1] + str(len(A) - cnt)
    ans = min(ans, len(encoding))

print(ans)