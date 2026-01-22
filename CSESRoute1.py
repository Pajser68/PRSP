n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [float('inf')] * (n + 1)
dist[1] = 0
visited = [False] * (n + 1)

for _ in range(n):
    u = -1
    for i in range(1, n + 1):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
    visited[u] = True
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

print(' '.join(str(dist[i]) for i in range(1, n + 1)))
