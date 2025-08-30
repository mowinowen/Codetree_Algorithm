n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n - 1, 0, -1):
    val = B[i] - A[i]
    for j in range(i - 1, -1, -1):
        if val - A[j] > 0:
            A[i] += A[j]
            ans += A[j] * (i - j)
            val -= A[j]
            A[j] = 0
        else:
            A[i] += val
            ans += val * (i - j)
            A[j] -= val
            val -= val
        
        if val == 0:
            break

print(ans)
        

'''
5 4 3 1
5 3 0 5


3 6 4 2 1
3 6 4 0 3 -> 2
3 6 2 0 5 -> 4
3 6 0 2 5 -> 2
3 5 0 3 5 -> 2
3 1 4 3 5 -> 4
2 2 4 3 5 -> 1
'''