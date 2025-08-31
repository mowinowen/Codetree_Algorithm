n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n):
    if A[i] > B[i]:
        ans += A[i] - B[i]
        A[i + 1] += A[i] - B[i]

print(ans)