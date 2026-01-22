import sys
sys.setrecursionlimit(1 << 25)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
graph_rev = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph_rev[b-1].append(a-1)

def dfs(u, visited, g):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v, visited, g)

visited = [False] * n
dfs(0, visited, graph)
if not all(visited):
    for i in range(n):
        if not visited[i]:
            print("NO")
            print(1, i+1)
            exit()

visited = [False] * n
dfs(0, visited, graph_rev)
if not all(visited):
    for i in range(n):
        if not visited[i]:
            print("NO")
            print(i+1, 1)
            exit()

print("YES")
