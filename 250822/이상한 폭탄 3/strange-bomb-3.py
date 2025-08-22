from collections import defaultdict

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

idx_dict = defaultdict(list)
for i, v in enumerate(nums):
    idx_dict[v].append(i)

ans, max_cnt = 0, 0
for k, idxs in idx_dict.items():
    cnt = sum(1 for i in range(1, len(idxs)) if idxs[i] - idxs[i-1] <= K)
    # print(cnt)
    if cnt > max_cnt or (cnt == max_cnt and cnt > 0 and k > ans):
        max_cnt, ans = cnt, k

print(ans)
