n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, x = map(int, input().split())
    edges.append((a, b, x))

INF = 10**18
score = [-INF] * (n + 1)
score[1] = 0

for _ in range(n - 1):
    for a, b, x in edges:
        if score[a] != -INF and score[b] < score[a] + x:
            score[b] = score[a] + x

# Detect positive cycles
reachable = [False] * (n + 1)
for _ in range(n):
    for a, b, x in edges:
        if score[a] != -INF and score[b] < score[a] + x:
            score[b] = INF
            reachable[b] = True

# Check if n is affected by a positive cycle
if score[n] == INF:
    print(-1)
else:
    print(score[n])