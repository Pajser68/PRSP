import heapq

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

heap = [(0, 1)]  # (cost, node)
dist = [[] for _ in range(n + 1)]  # store up to k shortest distances for each node

while heap:
    cost, u = heapq.heappop(heap)
    if len(dist[u]) >= k:
        continue
    dist[u].append(cost)
    for v, w in graph[u]:
        heapq.heappush(heap, (cost + w, v))

print(' '.join(map(str, dist[n][:k])))