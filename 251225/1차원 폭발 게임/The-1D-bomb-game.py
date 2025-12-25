from itertools import groupby

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
while True:
    isbool = False
    new_numbers = []

    for num, group in groupby(numbers):
        g_list = list(group)

        if len(g_list) >= m:
            isbool = True

        else:
            new_numbers += g_list
    
    numbers = new_numbers
    if not isbool:
        break

print(len(numbers))

for num in numbers:
    print(num)