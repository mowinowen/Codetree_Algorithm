from bisect import bisect_left
from collections import Counter

N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
count_dict = Counter(a)

ans = 0
for i in range(N, 0, -1):
    bl = bisect_left(a, i)
    if N - bl < i:
        cnt = count_dict[i - 1]
        if cnt <= L and cnt + N - bl >= i:
            ans = i
            break
    else:
        ans = i
        break
print(ans)
