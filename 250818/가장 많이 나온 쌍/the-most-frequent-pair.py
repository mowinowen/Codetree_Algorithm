from collections import defaultdict

n, m = map(int, input().split())
count_dict = defaultdict(int)

for _ in range(m):
    a, b = map(int, input().split())
    count_dict[(a, b)] += 1
    count_dict[(b, a)] += 1

ans = 0
for _, cnt in count_dict.items():
    ans = max(cnt, ans)

print(ans)