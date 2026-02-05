import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# Please write your code here.

bridges = sorted([tuple(map(int, input().split())) for _ in range(m)], key = lambda x : x[1])
players = [i for i in range(n + 1)]

for x, y in bridges:
    players[x], players[x + 1] = players[x + 1], players[x]

print(sum(players[i] > players[j] for i in range(1, n + 1) for j in range(i + 1, n + 1)))