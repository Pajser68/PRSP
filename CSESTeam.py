def bfs(start, graph, color, n):
    queue = [start]
    color[start] = 1
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                color[neighbor] = 3 - color[node]  # Alternate between 1 and 2
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [0] * (n + 1)
possible = True
for i in range(1, n + 1):
    if color[i] == 0:
        if not bfs(i, graph, color, n):
            possible = False
            break

if not possible:
    print("IMPOSSIBLE")
else:
    print(' '.join(str(color[i]) for i in range(1, n + 1)))