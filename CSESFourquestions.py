import sys
input = sys.stdin.readline

MOD = 10**9 + 7
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [float('inf')] * (n + 1)
ways = [0] * (n + 1)
min_flights = [float('inf')] * (n + 1)
max_flights = [0] * (n + 1)

visited = [False] * (n + 1)
dist[1] = 0
ways[1] = 1
min_flights[1] = 0
max_flights[1] = 0

for _ in range(n):
    u = -1
    for i in range(1, n + 1):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
    if dist[u] == float('inf'):
        break
    visited[u] = True
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            ways[v] = ways[u]
            min_flights[v] = min_flights[u] + 1
            max_flights[v] = max_flights[u] + 1
        elif dist[v] == dist[u] + w:
            ways[v] = (ways[v] + ways[u]) % MOD
            min_flights[v] = min(min_flights[v], min_flights[u] + 1)
            max_flights[v] = max(max_flights[v], max_flights[u] + 1)

print(dist[n], ways[n], min_flights[n], max_flights[n])