n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.

div = sum(blocks) // n
ans = 0
for block in blocks:
    if block > div:
        ans += block - div

print(ans)