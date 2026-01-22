import sys
sys.setrecursionlimit(2 * 10**5 + 10)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)
cycle = []

def dfs(u, p):
    visited[u] = True
    for v in graph[u]:
        if v == p:
            continue
        if visited[v]:
            # Found a cycle
            path = [u]
            x = u
            while x != v:
                x = parent[x]
                path.append(x)
            path.reverse()
            path.append(u)
            print(len(path))
            print(' '.join(map(str, path)))
            sys.exit(0)
        else:
            parent[v] = u
            dfs(v, u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, 0)

print("IMPOSSIBLE")