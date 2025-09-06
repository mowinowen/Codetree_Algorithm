from collections import Counter

n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
sort_a = sorted(set(a))
count_dict = Counter(a)
# print(count_dict)
# print(sort_a)

if len(count_dict) == 1 or count_dict[sort_a[1]] != 1:
    print(-1)

else:
    print(a.index(sort_a[1]) + 1)