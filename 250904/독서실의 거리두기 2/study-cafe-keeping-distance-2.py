N = int(input())
seats = list(input())

# Please write your code here.
seated = [i for i, j in enumerate(seats) if j == '1']
if len(seated) != 1:
    gaps = [seated[i] - seated[i - 1] for i in range(1, len(seated))]
    ans = min(max(gaps) // 2, min(gaps))

ans = max(seated[0] - 0, N - 1 - seated[-1], ans)
print(ans)