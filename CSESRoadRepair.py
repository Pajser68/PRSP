import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))
    graph[b-1].append((c, a-1))

visited = [False] * n
heap = [(0, 0)]  # (cost, node)
total = 0
count = 0

while heap:
    cost, u = heapq.heappop(heap)
    if visited[u]:
        continue
    visited[u] = True
    total += cost
    count += 1
    for edge_cost, v in graph[u]:
        if not visited[v]:
            heapq.heappush(heap, (edge_cost, v))

if count == n:
    print(total)
else:
    print("IMPOSSIBLE")