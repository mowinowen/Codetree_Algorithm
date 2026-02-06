import sys
from itertools import combinations
input = sys.stdin.readline

n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
info = []
for i in range(n):
    for j in range(n - m + 1):
        vals = []
        for k in range(j, j + m):
            vals.append((i, k))

        info.append(vals)

max_ans = 0
for i in range(len(info)):
    for j in range(i + 1, len(info)):
        if not set(info[i]) & set(info[j]):
            sum_val = 0
            ans = 0
            for x, y in info[i]:
                sum_val += weight[x][y]
            
            if sum_val > c:
                tmp_max = 0
                max_comb = []
                for k in range(1, m):
                    for comb in combinations(info[i], k):
                        tmp = 0
                        for x, y in comb:
                            tmp += weight[x][y]

                        if tmp <= c and tmp_max < tmp:
                            tmp_max = tmp
                            max_comb = comb
                for x, y in max_comb:
                    ans += weight[x][y] ** 2
            else:
                for x, y in info[i]:
                    ans += weight[x][y] ** 2

            sum_val = 0
            for x, y in info[j]:
                sum_val += weight[x][y]
            
            if sum_val > c:
                tmp_max = 0
                max_comb = []
                for k in range(1, m):
                    for comb in combinations(info[j], k):
                        tmp = 0
                        for x, y in comb:
                            tmp += weight[x][y]

                        if tmp <= c and tmp_max < tmp:
                            tmp_max = tmp
                            max_comb = comb
                for x, y in max_comb:
                    ans += weight[x][y] ** 2
            else:
                for x, y in info[j]:
                    ans += weight[x][y] ** 2

            max_ans = max(ans, max_ans)

print(max_ans)            