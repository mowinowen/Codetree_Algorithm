n, m, p = map(int, input().split())
people = set([chr(ord('A') + i) for i in range(n)])
info = []

for i in range(m):
    c, u = input().split()
    info.append((c, u))
    if i + 1 >= p:
        if c in people:
            people.remove(c)

if info[p - 2][1] == info[p - 1][1]:
    if info[p - 2][0] in people:
        people.remove(info[p - 2][0])

if info[p - 1][1] == '0':
    people = []

for c in sorted(list(people)):
    print(c, end= ' ')

'''
D E
C D E
C D E
B C D E

D
C D
C D
C D
C D
'''