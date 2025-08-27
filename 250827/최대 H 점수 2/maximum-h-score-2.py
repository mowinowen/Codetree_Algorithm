from bisect import bisect_left, bisect_right

N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
ans = 0
for i in range(1, 101):
    # print(i, N - bisect_left(a, i))
    if N - bisect_left(a, i) < i:
        cnt = 0
        for j in range(bisect_left(a, i) - 1, -1, -1):
            if a[j] == i - 1:
                cnt += 1
            else:
                break
        # print(i, cnt, cnt + N - bisect_left(a, i))
        if cnt <= L and cnt + N - bisect_left(a, i) >= i:
            ans = max(ans, i)
    else:
        ans = max(ans, i)
print(ans)

    
        