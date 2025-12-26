import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
while len(numbers) >= m:
    new_numbers = []
    curr_num = numbers[0]
    cnt = 1
    isbool = False

    for num in numbers[1:]:
        if num == curr_num:
            cnt += 1
        else:
            if cnt < m:
                new_numbers += [curr_num] * cnt
            else:
                isbool = True
            
            curr_num = num
            cnt = 1

    if cnt < m:
        new_numbers += [curr_num] * cnt
    else:
        isbool = True
    
    numbers = new_numbers
    if not isbool:
        break
                
print(len(numbers))
print(*numbers, sep='\n')