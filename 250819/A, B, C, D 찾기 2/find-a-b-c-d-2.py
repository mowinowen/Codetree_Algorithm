nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
a, b = nums[0], nums[1]

if a + b == nums[2]:
    c = nums[3]
else:
    c = nums[2]

d = nums[-1] - a - b - c

print(a, b, c, d)