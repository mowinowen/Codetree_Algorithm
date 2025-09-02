import bisect

N = int(input())
seats = list(input())

# Please write your code here.
# seated = [i for i, j in enumerate(seats) if j == '1']

# print(seated)
ans = float('-inf')
for i in range(1, N - 1):
    if seats[i] == '0':
        seats[i] = '1'
        seated = [i for i, j in enumerate(seats) if j == '1']
        
        curr = float('inf')
        for j in range(1, len(seated)):
            curr = min(seated[j] - seated[j - 1], curr)
        seats[i] = '0'
    
    ans = max(curr, ans)

print(ans)