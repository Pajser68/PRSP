n, m, q = map(int, input().split())
INF = 10**18

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
    # Dijkstra from node i
    used = [False] * (n + 1)
    d = dist[i][:]
    for _ in range(n):
        u = -1
        for v in range(1, n + 1):
            if not used[v] and (u == -1 or d[v] < d[u]):
                u = v
        if d[u] == INF:
            break
        used[u] = True
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
    dist[i] = d

for _ in range(q):
    a, b = map(int, input().split())
    print(dist[a][b] if dist[a][b] < INF else -1)