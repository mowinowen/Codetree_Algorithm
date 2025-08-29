n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, 1))
    segments.append((x2 + 1, -1))

segments.sort()

cnt = 0
isbool = False
for x, line in segments:
    cnt += line
    if cnt == n - 1:
        isbool = True
        print('Yes')
        break

if not isbool:
    print('No')