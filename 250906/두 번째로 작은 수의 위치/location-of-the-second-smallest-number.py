n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
sort_a = sorted(a)
count_dict = {}

for val in sort_a:
    if val not in count_dict:
        if len(count_dict) == 2:
            break
        count_dict[val] = 1
    else:
        count_dict[val] += 1

val_counts = tuple(count_dict.items())
if len(val_counts) == 1 or val_counts[-1][1] != 1:
    print(-1)

else:
    print(a.index(val_counts[-1][0]) + 1)