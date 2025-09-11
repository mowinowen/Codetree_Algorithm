n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
ans = 0
num = sequence[-1]

for i in range(n - 1, -1, -1):
    if num < sequence[i]:
        print(i + 1)
        break
    num = sequence[i]    