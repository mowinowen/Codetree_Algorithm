from itertools import groupby

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 1

while len(numbers) >= m:
    new_numbers = []
    curr_num = numbers[0]
    max_cnt = 0
    for num in numbers[1:]:
        if num == curr_num:
            cnt += 1
        else:
            if cnt < m:
                new_numbers += [curr_num] * cnt
            max_cnt = max(cnt, max_cnt)
            cnt = 1
            curr_num = num
    if cnt < m:
        new_numbers += [curr_num] * cnt
    max_cnt = max(cnt, max_cnt)
    numbers = new_numbers
    if max_cnt < m:
        break

print(len(numbers))
print(*numbers, sep='\n')