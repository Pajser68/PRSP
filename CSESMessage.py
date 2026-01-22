def bfs(start, end, graph, n):
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    queue = [start]
    visited[start] = True
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    return visited, parent

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited, parent = bfs(1, n, graph, n)

if not visited[n]:
    print("IMPOSSIBLE")
else:
    path = []
    curr = n
    while curr != 0:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))
