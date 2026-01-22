import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

INF = float('inf')
dist = [[INF, INF] for _ in range(n + 1)]
dist[1][0] = 0

heap = [(0, 1, 0)]  # (cost, node, used_coupon)

while heap:
    cost, u, used = heapq.heappop(heap)
    if dist[u][used] < cost:
        continue
    for v, w in graph[u]:
        # Move without using coupon
        if dist[v][used] > cost + w:
            dist[v][used] = cost + w
            heapq.heappush(heap, (dist[v][used], v, used))
        # Move using coupon (if not used yet)
        if used == 0:
            new_cost = cost + w // 2
            if dist[v][1] > new_cost:
                dist[v][1] = new_cost
                heapq.heappush(heap, (dist[v][1], v, 1))

print(dist[n][1])