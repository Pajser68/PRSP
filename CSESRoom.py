import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if grid[x][y] != '.':
        return
    grid[x][y] = '#'  # Mark as visited
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        dfs(x + dx, y + dy)

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

rooms = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            dfs(i, j)
            rooms += 1

print(rooms)