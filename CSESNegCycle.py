n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist = [0] * (n + 1)
parent = [-1] * (n + 1)
x = -1

for i in range(1, n + 1):
    x = -1
    for a, b, c in edges:
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            parent[b] = a
            x = b

if x == -1:
    print("NO")
else:
    # Reconstruct cycle
    for _ in range(n):
        x = parent[x]
    cycle = []
    cur = x
    while True:
        cycle.append(cur)
        if cur == x and len(cycle) > 1:
            break
        cur = parent[cur]
    cycle.reverse()
    print("YES")
    print(' '.join(map(str, cycle)))