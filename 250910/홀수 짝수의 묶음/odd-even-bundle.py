N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
odd = sum(num % 2 == 1 for num in numbers)
even = len(numbers) - odd

min_num = min(odd, even)
ans = min_num * 2

odd -= min_num
even -= min_num

if even != 0:
    ans += 1
elif odd != 0:
    if odd % 3 == 0:
        ans += 2 * (odd // 3)
    elif odd % 3 == 1:
        ans += 2 * (odd // 3) - 1
    else:
        ans += 2 * (odd // 3) + 1

print(ans)