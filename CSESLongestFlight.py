import sys
sys.setrecursionlimit(2 * 10**5 + 10)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# Topological sort (DFS)
visited = [False] * (n + 1)
order = []

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    order.append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
order.reverse()

# DP for longest path
dp = [-float('inf')] * (n + 1)
dp[1] = 1
parent = [-1] * (n + 1)

for u in order:
    for v in graph[u]:
        if dp[u] + 1 > dp[v]:
            dp[v] = dp[u] + 1
            parent[v] = u

if dp[n] == -float('inf'):
    print("IMPOSSIBLE")
else:
    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))