import sys
sys.setrecursionlimit(2 * 10**5 + 10)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * (n + 1)  # 0=unvisited, 1=visiting, 2=visited
order = []
possible = True

def dfs(u):
    global possible
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            dfs(v)
        elif visited[v] == 1:
            possible = False  # Found a cycle
    visited[u] = 2
    order.append(u)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)

if not possible:
    print("IMPOSSIBLE")
else:
    print(' '.join(map(str, reversed(order))))