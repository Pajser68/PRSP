import sys
sys.setrecursionlimit(2 * 10**5 + 10)
MOD = 10**9 + 7

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

# DP for number of ways
dp = [0] * (n + 1)
dp[1] = 1

for u in order:
    for v in graph[u]:
        dp[v] = (dp[v] + dp[u]) % MOD

print(dp[n])