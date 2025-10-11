import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]
pq = []

dist = [float('inf')] * (n + 1)

for i in range(m):
    x, y, z = edges[i]
    graph[x].append((y, z))
    graph[y].append((x, z))    

dist[k] = 0

heapq.heappush(pq, (0, k))
while pq:
    min_dist, min_index = heapq.heappop(pq)
    
    if min_dist != dist[min_index]:
        continue
    
    for i, d in graph[min_index]:
        new_dist = dist[min_index] + d
        if dist[i] > new_dist:
            dist[i] = new_dist
            heapq.heappush(pq, (new_dist, i))

for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])