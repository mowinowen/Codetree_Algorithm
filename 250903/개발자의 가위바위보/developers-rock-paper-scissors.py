from itertools import permutations

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    if a != b:
        arr.append((a, b))
ans = 0

for x, y, z in permutations(range(1, 4), 3):
    cnt = 0
    for a, b in arr:
        if a == y and b == x or a == z and b == y or a == x and b == z:
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)
