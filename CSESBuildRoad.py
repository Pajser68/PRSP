import sys
sys.setrecursionlimit(1 << 25)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False] * n
representatives = []

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

for i in range(n):
    if not visited[i]:
        representatives.append(i)
        dfs(i)

print(len(representatives) - 1)
for i in range(1, len(representatives)):
    # Connect each component to the previous one
    print(representatives[i-1]+1, representatives[i]+1)