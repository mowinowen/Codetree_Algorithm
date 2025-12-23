import sys
from itertools import groupby
input = sys.stdin.readline

A = input().strip()

# Please write your code here.
ans = float('inf')
A += A

for i in range(len(A) // 2):
    string = A[i : i + len(A) // 2]
    cnt = sum(len(str(len(list(b)))) + 1 for a, b in groupby(string))
    ans = min(ans, cnt)

print(ans)