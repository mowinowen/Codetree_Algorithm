import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
# Please write your code here.

bridges = []
for _ in range(m):
    x, y = map(int, input().split())
    bridges.append((x, y))

bridges.sort(key = lambda x : x[1])

players = [i for i in range(n + 1)]

for x, y in bridges:
    players[x], players[x + 1] = players[x + 1], players[x]

ans_players = players
isend = False
for i in range(m + 1):
    for new_bridges in combinations(bridges, i):
        players = [i for i in range(n + 1)]

        for x, y in new_bridges:
            players[x], players[x + 1] = players[x + 1], players[x]
        
        if players == ans_players:
            ans = i
            isend = True
            break
    
    if isend:
        break

print(ans)