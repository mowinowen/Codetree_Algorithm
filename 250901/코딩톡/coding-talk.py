n, m, p = map(int, input().split())
people = set([chr(ord('A') + i) for i in range(n)])
info = [tuple(input().split()) for _ in range(m)]

# print(info[p - 1])
for i in range(p - 1, m):
    if info[i][0] in people:
        people.remove(info[i][0])

for i in range(p - 2, -1, -1):
    if info[i][1] == info[p - 1][1]:
        if info[i][0] in people:
            people.remove(info[i][0])
    else:
        break

for p in sorted(list(people)):
    print(p, end=' ')
# print(people - {'B', 'C'})