N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.

min_h, max_h = min(heights), max(heights)
ans = float('inf')

for i in range(min_h, max_h - 16):
    curr_cost = 0
    for h in heights:
        if h < i:
            curr_cost += (i - h) ** 2
        elif h > i + 17:
            curr_cost += (h - i - 17) ** 2
    # print(curr_cost)
    ans = min(ans, curr_cost)

print(ans)