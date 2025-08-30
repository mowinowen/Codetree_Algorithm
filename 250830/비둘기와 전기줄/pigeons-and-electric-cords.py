n = int(input())
pigeon = {}
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    if not a in pigeon:
        pigeon[a] = b
    elif pigeon[a] != b:
        ans += 1
        pigeon[a] = b

print(ans)